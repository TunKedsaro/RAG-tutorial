import os
from google import genai

from utils.file_loader import load_file

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)


def contentquality_analyse(resume_json: str | None = None) -> str:
    print("File: contentqualtiy.py > def contentquality_analyse")

    # Download defual resume file for testing
    if resume_json is None or resume_json == "string":
        print("There are no correct resume_json format")
        print("Downloading defualt resume_json ...")
        resume_json = load_file("resume_json.txt")

    prompt = prompt = f"""
        You are an expert data career evaluator and resume reviewer.

        Evaluate the following resume content for **Content Quality**, focusing on five dimensions.
        For each dimension, provide:
        - A numeric score (0-20)
        - A brief explanation (2-3 sentences)
        - 1-2 improvement suggestions

        ### Scoring Guide
        - 0-5: Poor (mostly missing or irrelevant)
        - 6-10: Fair (partially meets expectations)
        - 11-15: Good (clear but needs more depth)
        - 16-20: Excellent (strong and well-written)

        ### Evaluation Dimensions
        1. **Quantifiable Impact**
        - Measures if achievements include measurable metrics (accuracy, F1-score, ROI, cost reduction, etc.)
        - Every bullet should ideally include numbers.

        2. **Skill Demonstration**
        - Evaluates whether each bullet shows what skill, tool, or technology was applied.
        - e.g., “Built face recognition system using Python and AWS”.

        3. **Specificity & Relevance**
        - Checks if statements are specific and relevant to the field.
        - Avoid vague phrases like “worked on many projects”; prefer “developed a fraud detection model using Random Forest”.

        4. **Grammar & Language Use**
        - Evaluates sentence clarity, grammar, and professional tone.
        - Prefer strong action verbs such as “Led”, “Designed”, “Implemented”.

        5. **Active Writing Style**
        - Checks for active-voice writing instead of passive.
        - e.g., “Created predictive model” vs “Was responsible for creating”

        ### Return Format (JSON only)
        {{
        "content_quality": {{
            "quantifiable_impact": {{
            "score": <0-20>,
            "explanation": "",
            "suggestions": []
            }},
            "skill_demonstration": {{
            "score": <0-20>,
            "explanation": "",
            "suggestions": []
            }},
            "specificity_and_relevance": {{
            "score": <0-20>,
            "explanation": "",
            "suggestions": []
            }},
            "grammar_and_language_use": {{
            "score": <0-20>,
            "explanation": "",
            "suggestions": []
            }},
            "active_writing_style": {{
            "score": <0-20>,
            "explanation": "",
            "suggestions": []
            }},
            "total_score": <0-100>
        }}
        }}

        ### Notes
        - Return only valid JSON.
        - Deduct points for vague wording or lack of measurable data.
        - Evaluate based on English and Thai if both appear.

        ### RESUME CONTENT ###
        {resume_json}
        """
    
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return resp.text
