import os
from google import genai

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")

client = genai.Client(api_key=API_KEY)

def section_level_analyse(resume_json: str) -> str:
    prompt = f"""
        You are an expert HR evaluator and resume reviewer.

        You will receive structured resume data in JSON format.
        Your task is to assign a completeness score (0–20) for each of the five major sections.

        ### Sections to evaluate:
        1. **Contact Information**
        2. **Professional Summary**
        3. **Education**
        4. **Experience**
        5. **Skills**

        ### Scoring Guide (0-20)
        - 0-5: Missing or minimal content
        - 6-10: Partial information (some fields empty or vague)
        - 11-15: Mostly complete with moderate detail
        - 16-20: Fully complete and rich in information (well-detailed, clear, professional)

        ### Evaluation Rules
        - Evaluate **content richness, completeness, and clarity**.
        - Missing fields or dashes (“-”) lower the score.
        - Count variety and depth (e.g., multiple education entries or skill levels add points).
        - Experience should reward both quantity and quality (e.g., clear responsibilities, bullet points).
        - Skills section should reward technical + soft skills + tools with levels.

        ### Return format (JSON only)
        {{
        "structure_score": {{
            "contact_information": {{
            "score": <0-20>,
            "explanation": ""
            }},
            "professional_summary": {{
            "score": <0-20>,
            "explanation": ""
            }},
            "education": {{
            "score": <0-20>,
            "explanation": ""
            }},
            "experience": {{
            "score": <0-20>,
            "explanation": ""
            }},
            "skills": {{
            "score": <0-20>,
            "explanation": ""
            }},
            "total_score": <0-100>
        }}
        }}
        ### IMPORTANT
        - Return **ONLY valid JSON**.
        - Do NOT add backticks.
        - Do NOT add explanations outside JSON.
        - Do NOT wrap the output in ```json ... ```.
        - Output must be raw JSON ONLY.
        ### Resume Data ###
        {resume_json}
        """
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return resp.text
