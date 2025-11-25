import os
from google import genai

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)

def load_default_resume():
    base_dir  = os.path.dirname(os.path.dirname(__file__))   # /code
    file_path = os.path.join(base_dir, "data", "resume_json.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def section_level_analyse(resume_json: str | None = None) -> str:
    if resume_json is None or resume_json == "string":
        print("There are no correct resume_json format")
        print("Downloading defualt resume_json ...")
        resume_json = load_default_resume()

    prompt = f"""
        You are an expert resume parser.

        From the following resume text, extract only the candidate's SKILLS as a clean Python list of strings.
        Include both technical (e.g., Python, SQL, Machine Learning) and non-technical (e.g., Communication, Leadership) skills if found.

        Return only valid JSON in this exact format:
        {{
            "skills":["skill1","skill2","skill3",...]
        }}

        Resume:
        {resume_json}
        """
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return resp.text
