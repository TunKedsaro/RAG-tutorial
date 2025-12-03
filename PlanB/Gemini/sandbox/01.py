from utils.file_loader import load_file
import yaml

with open("role.yaml", "r", encoding="utf-8") as f:
    role_prompt = yaml.safe_load(f)
with open("rule.yaml", "r", encoding="utf-8") as f:
    rule_prompt = yaml.safe_load(f)
with open("output.yaml", "r", encoding="utf-8") as f:
    output_prompt = yaml.safe_load(f)

role = role_prompt["role"]["standart"]
rule = rule_prompt["rule"]["standart"]
outp = output_prompt["output"]["test"]


class prompt_builder():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def build(self):
        jd = load_file("resume_json.txt")
        prompt = f'''Role : \n{self.x} \n\nRule :\n{self.y} \n\nOutput:\n{self.z}'''
        resume = f"\n\n{jd}"
        return prompt + resume

prompt = prompt_builder(role,rule,outp)
prompt = prompt.build()
# print(prompt)

from google import genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in environment")

client = genai.Client(api_key=API_KEY)

resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
print(resp.text)