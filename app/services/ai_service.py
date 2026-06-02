import time
from google import genai
from app.config import GEMINI_API_KEY
from app.logger import logger

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_ai(prompt: str) -> str:
    start = time.time()

    logger.info("Sending request to Gemini api for prompt " + prompt)

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=prompt
    )

    end = time.time()

    logger.info(f"Request took {end - start:.2f} seconds")

    return response.text