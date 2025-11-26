from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.gemini_client import analyse_text
from src.sectionlevel import section_level_analyse
from pydantic import BaseModel

class AnalyseRequest(BaseModel):
    text: str

app = FastAPI(
    title="CV/Resume Evaluation API",
    version="0.1.4",
    description=(
        "Microservices for CV/Resume evaluation (In progress krub)"
        "<br>"
        "Last time Update : 2511251951"
    ),
    contact={
        "name": "Tun Kedsaro",
        "email": "tun.k@terradigitalventures.com"
    },
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"message": "Ok I am ready"}

@app.post("/analyse")
def analyse(payload: AnalyseRequest):
    response = analyse_text(payload.text)
    return {"message": response}

@app.post("/sectionlevel")
def analyse(payload: AnalyseRequest):
    response = section_level_analyse(payload.text)
    return {"message": response}
