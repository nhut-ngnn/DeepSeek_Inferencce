import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import requests
from models.start_vllm import model


class QuestionRequest(BaseModel):
    question: str


def ask_model(question: str):
    """
    Sends a request to the model server and fetches a response.
    """
    url = "http://localhost:8000/v1/chat/completions"  
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  
    return response.json()

result = ask_model("What is the capital of France?")
print(json.dumps(result, indent=2))

def stream_llm_response(question:str):
    url = "http://localhost:8000/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "messages": [{"role": "user", "content": question}],
        "stream": True  
    }

    with requests.post(url, headers=headers, json=data, stream=True) as response:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8").replace("data: ", "")
                yield decoded_line + "\n"