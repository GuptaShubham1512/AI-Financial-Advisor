from config import MODEL_NAME
import google.generativeai as genai

model = genai.GenerativeModel(MODEL_NAME)

def test_connection():
    response = model.generate_content("Say hello")
    return response.text