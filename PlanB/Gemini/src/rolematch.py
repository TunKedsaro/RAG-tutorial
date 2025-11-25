import os
from google import genai

from utils.file_loader import load_file

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)

def rolematch_analyse(resume_json: str | None = None) -> str:
    print("File: contentqualtiy.py>def rolematch_analyse")

    prompt = prompt = f"""
        Just return 'Role match In progress krub'
        """
    
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return resp.text

