import os
from google import genai

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)

def analyse_text(text: str) -> str:
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text,
    )
    return resp.text

