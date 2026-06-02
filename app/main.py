from fastapi import FastAPI,HTTPException
from app.models.chat_request import ChatRequest
from app.services.ai_service import ask_ai

app = FastAPI()

@app.post("/chat/")
def chat(request: ChatRequest):
    try:

        response = ask_ai(request.prompt)

        return{
            "response": response
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        # return {
        #     "error":str(e)
        # }

@app.get("/")
def home():
    return{"Chat API is running."}