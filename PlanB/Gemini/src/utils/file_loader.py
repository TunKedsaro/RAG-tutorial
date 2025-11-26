print("/code/src/utils/file_loader.py")
import os

def load_file(filename: str) -> str:
    print("/code/src/utils/file_loader.py > def load_file")
    """
    Generic helper to load any file from /data folder.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  
    print(base_dir)
    file_path = os.path.join(base_dir, "data", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
