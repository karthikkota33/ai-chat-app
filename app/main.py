from fastapi import FastAPI,HTTPException
from app.models.chat_request import ChatRequest
from app.services.ai_service import ask_ai
from app.logger import logger

app = FastAPI()
chat_history = []

@app.post("/chat/")
def chat(request: ChatRequest):
    try:
        chat_history.append({
            "role":"user",
            "content":request.prompt
        })

        context =""
        for message in chat_history:
            context += f"{message['role']}:{message['content']}\n"
        # append the latest prompt and send
        full_prompt = context +f"user:{request.prompt}"
        response = ask_ai(full_prompt)

        chat_history.append({
            "role":"application",
            "content":response
        })

        logger.info(chat_history)

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