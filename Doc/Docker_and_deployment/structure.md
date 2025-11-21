<pre>
Folders
|- .devcontainer
|    |- devcontainer.json
|- src
|    |- smokeTest
|    |    |- __init__py
|    |    |- router.py
|    |- main.py
|- requirements.txt
</pre>
##### devcontainer.json
<pre>
{
    "name": "Python FastAPI Devcontainer",
    "build": {
        "dockerfile": "../Dockerfile.dev"
    },
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-python.vscode-pylance",
                "ms-python.black-formatter",
                "ms-python.debugpy",
                "ms-azuretools.vscode-docker"
            ],
            "settings": {}
        }
    },
    "forwardPorts": [
        "5678:5678"
    ],
    "workspaceMount": "source=${localWorkspaceFolder},target=/code,type=bind,consistency=delegated",
    "workspaceFolder": "/code",
    "runArgs": []
}
</pre>
##### init.py
from .router import *

##### main.py
<pre>
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest
import debugpy

debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(smokeTest.router, prefix="/smoke-test")

# Define the API endpoints
@app.get('/')
def health():
    return {
        "message": "OK 🚀"
    }
</pre>

##### router.py
<pre>
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ResponseBody(BaseModel):
    message: str

@router.get("/hello-world")
def prompt() -> ResponseBody:
    return {"message": "Hello, world!"}
</pre>

##### requirements.txt
fastapi>=0.110.0,<0.111.0
uvicorn>=0.29.0,<1.0.0
debugpy>=1.8.0,<2.0.0



