import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# API Key configuration
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_nutrition_tip_with_flash(goal: str) -> str:
    # ✅ Correct model name format
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = (
        f"Give one clear, helpful nutrition or recovery tip for someone focused on '{goal}'. "
        f"The tip should be practical, friendly, and easy to understand."
    )
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        # Fallback option: gemini-1.5-flash-latest allengil gemini-pro try cheyyunnu
        try:
            fallback_model = genai.GenerativeModel("gemini-1.5-flash-latest")
            response = fallback_model.generate_content(prompt)
            return response.text.strip()
        except Exception:
            return f"Tip: Stay hydrated and maintain a balanced diet for your goal: {goal}."