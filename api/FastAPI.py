from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import getpass
from models.start_vllm import model
from models.test_model import QuestionRequest, ask_model, stream_llm_response
from pyngrok import ngrok, conf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {'hello': 'world'}
@app.post("/api/v1/generate-response")
def generate_response(request: QuestionRequest):
    """
    API endpoint to generate a response from the model.
    """
    try:
        response = ask_model(request.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/generate-response-stream")
def stream_response(request:QuestionRequest):

  try:
    response = stream_llm_response(request.question)
    return StreamingResponse(response, media_type="text/event-stream")
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))