from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta

from src.service.gemini_client import analyse_text             # 0 Health check
from src.service.expmatch import expmatch_analyse              # API 01 : Criteria 1.1 : Experience matching
# from src.skillmatch import skill_match_analyse       # API 02 : Criteria 1.2 : Skill matching
# from src.rolematch import rolematch_analyse          # API 03 : Criteria 1.3 : Role matching
from src.service.contentquality import contentquality_analyse  # API 04 : Criteria 2.0 : Content quality
from src.service.sectionlevel import section_level_analyse     # API 05 : Criteria 3.0 : Section-Level

from src.utils.file_loader import load_json


class AnalyseRequest(BaseModel):
    JSON: str | None = None

app = FastAPI(
    title="CV/Resume Evaluation API",
    version="0.1.4",
    description=(
        "Microservices for CV/Resume evaluation (In progress krub)"
        "<br>"
        f"Last time Update : {str(datetime.now(tz=(timezone(timedelta(hours=7)))))}"
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
@app.get("/", tags=["Check"])
def health_Fastapi():
    print(f"File: main.py -> def health_Fastapi")
    return {"message": "Ok FastAPI is ready"}

# Health check
@app.post("/health_Gemini", tags=["Check"])
def hellth_Gemini(payload: AnalyseRequest = AnalyseRequest(
    text="This is Gemini connection test just return 'Gemini API is connected !!!'"
)):
    print(f"File: main.py -> def hellth_Gemini")
    response = analyse_text(payload.text)
    return {"message": response}

# FastAPI structure
@app.get("/output/testing1", tags=["Output format (mockup)"])
def Output_testing():
    print(f"File: main.py -> def Output_testing")
    return {
            "message": {
                        "Role_Relevance": {
                            "1_1_Role_Matching": {
                                "Score": 7,
                                "Feedback": "Role and education show partial alignment."
                            },
                            "1_2_Skill_Match": {
                                "Score": 3,
                                "Feedback": "Some skills overlap the required role skills."
                            },
                            "1_3_Experience_Matching": {
                                "Score": 9,
                                "Feedback": "Experience has moderate relevance to job requirements."
                            },
                            "1_4_Education_Relevance": {
                                "Score": 5,
                                "Feedback": "Education relevance is low for this role."
                            }
                        },
                        "Content_Quality": {
                            "2_1_Quantifiable_Impact": {
                                "Score": 1,
                                "Feedback": "No quantifiable impact found in the bullet points."
                            },
                            "2_2_Skill_Demonstration": {
                                "Score": 8,
                                "Feedback": "Candidate demonstrates clear technical skills in bullet points."
                            },
                            "2_3_Specificity_Relevance": {
                                "Score": 4,
                                "Feedback": "Descriptions are specific but can include more clarity."
                            },
                            "2_4_Grammar_Language": {
                                "Score": 6,
                                "Feedback": "Grammar and language usage are acceptable."
                            }
                        },
                        "Section_Level_Criteria": {
                            "3_1_Contact_Information": {
                                "Score": 2,
                                "Feedback": "Contact details mostly complete; some links missing."
                            },
                            "3_2_Education": {
                                "Score": 10,
                                "Feedback": "Education details provided but missing honors or GPA."
                            },
                            "3_3_Experience_Section": {
                                "Score": 0,
                                "Feedback": "Experience bullets need more structure and clarity."
                            },
                            "3_4_Skills_Section": {
                                "Score": 7,
                                "Feedback": "Skills section is complete and properly categorized."
                            }
                        }
                    }
        }



# API 01 : Criteria 1.1 : Experience matching
@app.post("/evaluation/experience", tags=["Evaluation"])
def evaluate_experience(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_experience")
    response = expmatch_analyse(payload.text)
    return {"message": response}

# # API 02 : Criteria 1.2 : Skill matching
# @app.post("/evaluation/skills", tags=["Evaluation"])
# def evaluate_skills(payload: AnalyseRequest):
#     print(f"File: main.py -> def evaluate_skills")
#     response = skill_match_analyse(payload.text)
#     return {"message": response}

# # API 03 : Criteria 1.3 : Role matching
# @app.post("/evaluation/role", tags=["Evaluation"])
# def evaluate_role(payload: AnalyseRequest):
#     print(f"File: main.py -> def evaluate_role")
#     response = rolematch_analyse(payload.text)
#     return {"message": response}

# API 04 : Criteria 2.0 : Content quality
@app.post("/evaluation/contentquality", tags=["Evaluation"])
def evaluate_content_quality(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_content_quality")
    response = contentquality_analyse(payload.text)
    return {"message": response}


# API 05 : Criteria 3.0 : Section-Level
@app.post("/evaluation/sectionlevel", tags=["Evaluation"])
def evaluate_section_level(payload: AnalyseRequest):
    print(f"File: main.py -> def evaluate_section_level")
    response = section_level_analyse(payload.text)
    return {"message": response}


import yaml

# model:
#     provider: "google"
#     embedding_model: "text-embedding-004"
#     generation_model: "gemini-2.5-flash"

# FastAPI structure
@app.get("/config/status", tags=["Admin"])
def config_status():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return {"config":config}


# class UpdateModelConfig(BaseModel):
#     provider: str | None = None
#     embedding_model: str | None = None
#     generation_model: str | None = None

# CONFIG_PATH = "config/model.yaml"


# @app.put("/config/models", tags=["Admin"])
# def update_model_config(payload: UpdateModelConfig):
#     with open(CONFIG_PATH, "r", encoding="utf-8") as f:
#         config = yaml.safe_load(f)

#     # Update only fields that user sends
#     if payload.provider is not None:
#         config["model"]["provider"] = payload.provider
#     if payload.embedding_model is not None:
#         config["model"]["embedding_model"] = payload.embedding_model
#     if payload.generation_model is not None:
#         config["model"]["generation_model"] = payload.generation_model

#     # Write back to YAML
#     with open(CONFIG_PATH, "w", encoding="utf-8") as f:
#         yaml.dump(config, f, sort_keys=False)

#     return {"message": "Model config updated", "config": config}

