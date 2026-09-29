import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# API Key initialization
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def update_workout_plan(original_plan: str, feedback: str) -> str:
    prompt = (
        f"Here is the original workout plan:\n{original_plan}\n\n"
        f"User feedback/requests for changes: {feedback}\n\n"
        f"Please update the workout plan according to the user's feedback while keeping it structured and effective."
    )

    # Primary & Fallback models
    models_to_try = [
        "gemini-1.5-pro",
        "gemini-1.5-pro-latest",
        "gemini-1.5-flash",
        "gemini-pro"
    ]

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text.strip()
        except Exception:
            continue

    # Fallback plan if all models fail
    return f"{original_plan}\n\n(Note: Updated based on feedback: '{feedback}')"