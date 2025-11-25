from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.gemini_client import analyse_text
from src.sectionlevel import section_level_analyse
from src.skillmatch import skill_match_analyse
from src.expmatch import expmatch_analyse
from src.contentquality import contentquality_analyse
from src.rolematch import rolematch_analyse
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

# FastAPI structure
@app.get("/")
def health_Fastapi():
    print(f"File: main.py -> def health_Fastapi")
    return {"message": "Ok FastAPI is ready"}

# Health check
@app.post("/health_Gemini")
def hellth_Gemini(payload: AnalyseRequest = AnalyseRequest(
    text="This is Gemini connection test just return 'Gemini API is connected !!!'"
)):
    print(f"File: main.py -> def hellth_Gemini")
    response = analyse_text(payload.text)
    return {"message": response}

# API 01 : Criteria 1.1 : Experience matching
@app.post("/evaluation/experience")
def evaluate_experience(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_experience")
    response = expmatch_analyse(payload.text)
    return {"message": response}

# API 02 : Criteria 1.2 : Skill matching
@app.post("/evaluation/skills")
def evaluate_skills(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_skills")
    response = skill_match_analyse(payload.text)
    return {"message": response}

# API 03 : Criteria 1.3 : Role matching
@app.post("/evaluation/role")
def evaluate_role(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_role")
    response = rolematch_analyse(payload.text)
    return {"message": response}

# API 04 : Criteria 2.0 : Content quality
@app.post("/evaluation/contentquality")
def evaluate_content_quality(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_content_quality")
    response = contentquality_analyse(payload.text)
    return {"message": response}

# API 05 : Criteria 3.0 : Section-Level
@app.post("/evaluation/sectionlevel")
def evaluate_section_level(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_section_level")
    response = section_level_analyse(payload.text)
    return {"message": response}