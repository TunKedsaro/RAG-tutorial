import os
from google import genai
import json

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)


def load_default_resume():
    print("File: expmatch.py>def load_default_resume")

    base_dir  = os.path.dirname(os.path.dirname(__file__))   # /code
    file_path = os.path.join(base_dir, "data", "resume_json.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
def load_default_jd():
    print("File: expmatch.py>def load_default_jd")

    base_dir  = os.path.dirname(os.path.dirname(__file__))   # /code
    file_path = os.path.join(base_dir, "data", "jd_text.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def expmatch_analyse(resume_json: str | None = None) -> str:
    print("File: expmatch.py>def expmatch_analyse")

    if resume_json is None or resume_json == "string":
        print("There are no correct resume_json format")
        print("Downloading defualt resume_json ...")
        resume_json = load_default_resume()

    jd_text = load_default_jd()
    prompt = f"""
        You are an HR evaluation assistant specialized in data science recruitment.

        You will be given:
        1. A job description (JD)
        2. A candidate's extracted resume data in JSON format

        Your task:
        - Compare the candidate's experience, skills, and qualifications against the JD requirements.
        - Focus on *experience relevance*, not education or soft skills.
        - Evaluate how closely the candidate's actual experience and technical skills match the job's responsibilities and required tools.
        - Consider alignment in tools (Python, SQL, PySpark, Power BI, etc.), ML techniques, data pipeline experience, and communication requirements.

        Output format (JSON only):

        {{
        "experience_relevance_score": <0-50>,
        "explanation": [
            "Matched on machine learning and NLP experience.",
            "Has Python and SQL but no PySpark or cloud platform experience.",
            "Good visualization tools but limited big data exposure."
        ]
        }}

        Scoring guide:
        - 0-10: Very low relevance (different domain or junior)
        - 11-25: Partial match (some skills overlap)
        - 26-40: Good fit (most tools and responsibilities match)
        - 41-50: Excellent fit (direct match to required experience)

        ### JOB DESCRIPTION ###
        {jd_text}

        ### CANDIDATE RESUME ###
        {resume_json}
        """
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return resp.text

