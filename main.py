from fastapi import FastAPI
from pydantic import BaseModel
import app.routes.test as test

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
    answer.response = await test.detect_intent("testagent-wfsa", "123456", message.text, "pt-br")
    return answer.response
