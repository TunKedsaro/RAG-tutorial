print("/code/src/utils/file_loader.py")
# import os
# import json

# def load_file(filename: str) -> str:
#     print("/code/src/utils/file_loader.py > def load_file")
#     """
#     Generic helper to load any file from /data folder.
#     """
#     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  
#     print(base_dir)
#     file_path = os.path.join(base_dir, "data", filename)
#     with open(file_path, "r", encoding="utf-8") as f:
#         return f.read()


import os
import json
import yaml

def get_project_root():
    # __file__ = /code/src/utils/file_loader.py
    # go up 3 levels → /code
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_file(filename: str) -> str:
    base_dir = get_project_root()          # /code
    file_path = os.path.join(base_dir, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_json(filename: str) -> dict:
    base_dir = get_project_root()          # /code
    file_path = os.path.join(base_dir, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(filename: str):
    base_dir = get_project_root()
    file_path = os.path.join(base_dir, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
