from fastapi import FastAPI,HTTPException
from app.models.chat_request import ChatRequest
from app.services.ai_service import ask_ai
from app.logger import logger

app = FastAPI()
MAX_HISTORY = 10
# chat_history = []
chat_sessions={}

@app.post("/chat/")
def chat(request: ChatRequest):
    try:
        # chat_history.append({
        #     "role":"user",
        #     "content":request.prompt
        # })
        # If userId not found add in the sessions dictionary  
        user_id = request.user_id
        if user_id not in chat_sessions:
            chat_sessions[user_id]=[]

        if len(chat_sessions[user_id]) > MAX_HISTORY:
            chat_sessions[user_id].pop(0)

        chat_sessions[user_id].append({
            "role":"user",
            "content":request.prompt
        })

        context =""
        for message in chat_sessions[user_id]:
            context += f"{message['role']}:{message['content']}\n"
        # append the latest prompt and send
        # commenting as latest prompt already added to session
        # full_prompt = context +f"user:{request.prompt}"
        response = ask_ai(context)

        chat_sessions[user_id].append({
            "role":"assistant",
            "content":response
        })

        # chat_history.append({
        #     "role":"application",
        #     "content":response
        # })

        # if len(chat_history) > MAX_HISTORY:
        #     chat_history.pop(0)

        if len(chat_sessions[user_id]) > MAX_HISTORY:
            chat_sessions[user_id].pop(0)

        # logger.info(f"History Size: {len(chat_history)}")

        logger.info(chat_sessions)

        logger.info(f"User {user_id} has {len(chat_sessions[user_id])} messages")

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