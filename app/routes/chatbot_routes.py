from fastapi import FastAPI
from pydantic import BaseModel
from test import detect_intent

app = FastAPI()

class Message(BaseModel):
    text: str
    email: str
    sessionID: str
    
class Answer(BaseModel):
    response: str

@app.post("/send-message")
async def send_message(message: Message):
    answer = Answer
    answer.response = await detect_intent("testagent-wfsa", "123456", "olá", "pt-br")
    return answer.response
