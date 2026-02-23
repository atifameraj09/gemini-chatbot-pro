import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

def get_gemini_response(prompt, chat_history):
    chat = model.start_chat(history=chat_history)
    response = chat.send_message(prompt)
    return response.text