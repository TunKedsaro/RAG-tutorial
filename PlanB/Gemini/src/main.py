from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.gemini_client import analyse_text
from src.sectionlevel import section_level_analyse
from pydantic import BaseModel


from src.skillmatch import section_level_analyse

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

# FastAPI structure
@app.get("/")
def health_Fastapi():
    return {"message": "FastAPI is ready"}

# Health check
@app.post("/health_Gemini")
def hellth_Gemini(payload: AnalyseRequest = AnalyseRequest(
    text="This is Gemini connection test just return 'Gemini API is connected !!!'"
)):
    response = analyse_text(payload.text)
    return {"message": response}

# API 1 : 
@app.post("/sectionlevel")
def analyse(payload: AnalyseRequest):
    response = section_level_analyse(payload.text)
    return {"message": response}

# API 2 : 
@app.post("/skillmatch")
def skillmatch_analyse(payload: AnalyseRequest):
    # print(payload.text)
    response = section_level_analyse(payload.text)
    return {"message": response}

