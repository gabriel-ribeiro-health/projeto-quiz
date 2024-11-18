from typing import List
from fastapi import APIRouter, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from config.redis_config import get_redis_connection
import time

# Criação do roteador para endpoints de votação
router = APIRouter()
redis_conn = get_redis_connection()

class Vote(BaseModel):
    student_id: str
    question_id: str
    option_id: str

@router.post("/vote")
def register_vote(vote: Vote):
    redis_conn = get_redis_connection()

    vote_key = f"votes:{vote.question_id}"
    option_key = f"option:{vote.question_id}:{vote.option_id}"

    # Validar se a alternativa existe
    if not redis_conn.exists(option_key):
        raise HTTPException(status_code=404, detail="Alternativa não encontrada.")

    # Registrar o voto no Redis
    timestamp = int(time.time() * 1000)  # Tempo em milissegundos
    redis_conn.zadd(vote_key, {f"{vote.student_id}:{vote.option_id}": timestamp})

    # Incrementar a contagem de votos na alternativa
    redis_conn.hincrby(option_key, "votes", 1)  # Atualiza o campo 'votes'

    return {"message": "Voto registrado com sucesso!"}



from typing import Dict

class Question(BaseModel):
    question_id: str
    text: str
    options: Dict[str, str]


@router.post("/questions")
def create_question(question: Question):
    redis_conn = get_redis_connection()

    # Criar a pergunta
    redis_conn.hset(f"question:{question.question_id}", mapping={
        "text": question.text,
        "options": ",".join(question.options.keys())
    })
    redis_conn.expire(f"question:{question.question_id}", 2592000)

    # Criar alternativas
    for option_key, option_text in question.options.items():
        redis_conn.hset(f"option:{question.question_id}:{option_key}", mapping={
            "text": option_text,
            "votes": 0
        })
        redis_conn.expire(f"option:{question.question_id}:{option_key}", 2592000)

    return {"message": "Pergunta criada com sucesso!"}


from typing import List

class BulkQuestions(BaseModel):
    questions: List[Question]

@router.post("/questions/bulk")
def create_bulk_questions(data: BulkQuestions):
    for question in data.questions:
        create_question(question)
    return {"message": "Perguntas criadas com sucesso!"}



@router.get("/rankings/alternatives")
def get_alternative_rankings():
    redis_conn = get_redis_connection()
    rankings = []

    # Iterar pelas alternativas de cada pergunta
    for question_id in range(1, 11):  # Para perguntas de 1 a 10
        for option_id in ["A", "B", "C", "D"]:  # Opções fixas
            option_key = f"option:{question_id}:{option_id}"
            if redis_conn.exists(option_key):  # Verifica se a chave da alternativa existe
                alternative_data = redis_conn.hgetall(option_key)
                text = alternative_data[b'text'].decode()
                votes = int(alternative_data[b'votes'].decode())
                rankings.append({
                    "question_id": question_id,
                    "alternative": option_id,
                    "text": text,
                    "votes": votes
                })

    # Ordenar pelo número de votos
    rankings.sort(key=lambda x: x["votes"], reverse=True)
    return {"rankings": rankings}


@router.get("/rankings/questions")
def get_question_rankings():
    redis_conn = get_redis_connection()
    rankings = []

    # Alternativas corretas para as perguntas
    correct_answers = {
        "1": "C", "2": "B", "3": "B", "4": "B", "5": "B",
        "6": "C", "7": "C", "8": "C", "9": "B", "10": "B"
    }

    # Calcular acertos por questão
    for question_id, correct_option in correct_answers.items():
        vote_key = f"votes:{question_id}"
        votes = redis_conn.zrangebyscore(vote_key, min=0, max=float('inf'))

        # Contar acertos para a questão
        correct_count = sum(1 for vote in votes if f":{correct_option}".encode() in vote)
        rankings.append({"question_id": question_id, "correct_count": correct_count})

    # Ordenar pelo número de acertos
    rankings.sort(key=lambda x: x["correct_count"], reverse=True)
    return {"rankings": rankings}


@router.get("/rankings/students")
def get_student_rankings():
    redis_conn = get_redis_connection()

    # Alternativas corretas para cada pergunta
    correct_answers = {
        "1": "C", "2": "B", "3": "B", "4": "B", "5": "B",
        "6": "C", "7": "C", "8": "C", "9": "B", "10": "B"
    }

    student_scores = {}  # Para acumular acertos e tempos

    # Processar votos por questão
    for question_id, correct_option in correct_answers.items():
        vote_key = f"votes:{question_id}"
        votes = redis_conn.zrangebyscore(vote_key, min=0, max=float('inf'), withscores=True)

        for vote_data, timestamp in votes:
            student_id, voted_option = vote_data.decode().split(":")
            if student_id not in student_scores:
                student_scores[student_id] = {"correct_count": 0, "total_time": 0, "vote_count": 0}

            # Incrementar acertos se a alternativa for correta
            if voted_option == correct_option:
                student_scores[student_id]["correct_count"] += 1

            # Atualizar tempo total e contagem de votos
            student_scores[student_id]["total_time"] += timestamp
            student_scores[student_id]["vote_count"] += 1

    # Calcular métricas
    for student_id, scores in student_scores.items():
        scores["average_time"] = scores["total_time"] / scores["vote_count"] if scores["vote_count"] > 0 else 0

    # Rankings
    by_correct = sorted(student_scores.items(), key=lambda x: x[1]["correct_count"], reverse=True)
    by_speed = sorted(student_scores.items(), key=lambda x: x[1]["average_time"])
    combined = sorted(student_scores.items(), key=lambda x: (x[1]["correct_count"], -x[1]["average_time"]), reverse=True)

    return {
        "by_correct": [{"student_id": s[0], "correct_count": s[1]["correct_count"]} for s in by_correct],
        "by_speed": [{"student_id": s[0], "average_time": s[1]["average_time"]} for s in by_speed],
        "combined": [{"student_id": s[0], "correct_count": s[1]["correct_count"], "average_time": s[1]["average_time"]} for s in combined]
    }

