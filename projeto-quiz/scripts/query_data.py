from config.redis_config import get_redis_connection

def query_quiz(quiz_id):
    redis_conn = get_redis_connection()

    # Obter informações do quiz
    quiz_data = redis_conn.hgetall(f'quiz:{quiz_id}')
    print("Quiz:", {k.decode(): v.decode() for k, v in quiz_data.items()})

    # Obter perguntas associadas ao quiz
    question_ids = quiz_data[b'questions'].decode().split(',')
    for question_id in question_ids:
        question_data = redis_conn.hgetall(f'question:{question_id}')
        print(f"Pergunta {question_id}:", {k.decode(): v.decode() for k, v in question_data.items()})

if __name__ == '__main__':
    query_quiz(1)
