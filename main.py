from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

class Question(BaseModel):
    question_text: str
    question_id: int


@app.get("/question/{question_key}")
def get_question(question_key: str):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)    
    return r.hgetall("question:"+question_key)


@app.post("/question")
def create_question(question: Question):
    # connect to redis localhost
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    
    # Use the data from the request body
    r.hset(f'question:{question.question_id}', 'question_text', question.question_text)

    return {"message": "Question has been created"}