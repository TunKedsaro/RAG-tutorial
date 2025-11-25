from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from src.gemini_client import analyse_text
from src.sectionlevel import section_level_analyse
from src.skillmatch import skill_match_analyse
from src.expmatch import expmatch_analyse
from src.contentquality import contentquality_analyse

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
def sectionlevel_microservice(payload: AnalyseRequest):
    response = section_level_analyse(payload.text)
    return {"message": response}

# API 2 : 
@app.post("/skillmatch")
def skill_microservice(payload: AnalyseRequest):
    print("File: main.py>def skillmatch_analyse")
    # print(payload.text)
    response = skill_match_analyse(payload.text)
    return {"message": response}

# API 3 : 
@app.post("/expmatch")
def exp_microservice(payload: AnalyseRequest):
    print("File: main.py>def expmatch_analyse")
    response = expmatch_analyse(payload.text)
    return {"message": response}

# API 4 : 
@app.post("/contentquality")
def contentquality_microservice(payload: AnalyseRequest):
    print("File: main.py>def expmatch_analyse")
    response = contentquality_analyse(payload.text)
    return {"message": response}