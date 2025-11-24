from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.gemini_client import analyse_text
from pydantic import BaseModel

class AnalyseRequest(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"message": "I am ready"}

@app.post("/analyse")
def analyse(payload: AnalyseRequest):
    response = analyse_text(payload.text)
    return {"message": response}
