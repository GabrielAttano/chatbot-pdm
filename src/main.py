from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.service.dialogflowService import DialogflowController
from src.model.message import *

app = FastAPI()
    
@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}

@app.post("/send-message")
async def send_message(message: Message):
    answer = Answer(
        botResponse = await DialogflowController.detect_intent("bsf-chatbot-hipk", message.sessionID, message.text, "pt-br")
        )
    return answer