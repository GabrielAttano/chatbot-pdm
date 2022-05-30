from pydantic import BaseModel

class Message(BaseModel):
    text: str
    email: str
    sessionID: str

class Answer(BaseModel):
    botResponse: str