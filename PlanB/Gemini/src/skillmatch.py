import os
from google import genai
import json

# Deploy mode
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")
client = genai.Client(api_key=API_KEY)


Iskills = ["Python", "R", "SQL", "Scala", "Julia", "Java",
"Linear Algebra", "Calculus", "Probability", "Descriptive Statistics", "Inferential Statistics", "Hypothesis Testing", "Bayesian Statistics",
"Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Neural Networks", "Convolutional Neural Networks (CNN)", "Recurrent Neural Networks (RNN)", "Transformers", "Gradient Boosting", "Decision Trees", "Ensemble Learning", "Feature Engineering", "Model Evaluation", "Hyperparameter Tuning",
"Pandas", "NumPy", "Scikit-learn", "SciPy", "Statsmodels", "Dask", "Polars",
"Matplotlib", "Seaborn", "Plotly", "Power BI", "Tableau", "ggplot2", "Altair", "Dash",
"MySQL", "PostgreSQL", "MongoDB", "Hadoop", "Spark", "Hive", "Snowflake", "BigQuery", "Redshift",
"AWS", "GCP", "Azure", "Docker", "Kubernetes", "CI/CD", "MLflow", "DVC", "Kubeflow", "SageMaker", "Vertex AI",
"ETL", "Data Warehousing", "Airflow", "Kafka", "Data Pipeline Design",
"Text Preprocessing", "Tokenization", "Word Embeddings", "Transformers", "BERT", "LLMs", "Sentiment Analysis", "Topic Modeling",
"Communication", "Problem Solving", "Critical Thinking", "Storytelling with Data", "Business Acumen", "Collaboration",
"Git", "GitHub", "Jupyter Notebook", "VS Code", "PyCharm", "Linux", "Bash",
"Finance", "Healthcare", "Marketing Analytics", "Supply Chain", "Geospatial Analysis", "Computer Vision"]

def load_default_resume():
    print("File: skillmatch.py>def load_default_resume")

    base_dir  = os.path.dirname(os.path.dirname(__file__))   # /code
    file_path = os.path.join(base_dir, "data", "resume_json.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def skill_match_analyse(resume_json: str | None = None) -> str:
    print("File: skillmatch.py>def section_level_analyse")

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
    # return resp.text

    Rskills = json.loads(resp.text.split('```json')[1].split('```')[0])
    Rskills = Rskills['skills']

    Rsk = set(Rskills)
    Isk = set(Iskills)

    score = len(Rsk&Isk)
    # print(f"score : {score/len(Isk):.5f} ({score}/{len(Isk)})")
    point_skill_match = score/len(Isk)*50
    return point_skill_match
    # print(resume_json)
