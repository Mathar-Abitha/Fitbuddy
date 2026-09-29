import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# API Key initialization
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_workout_gemini(user_input: dict) -> str:
    goal = user_input.get("goal", "general fitness")
    intensity = user_input.get("intensity", "moderate")

    prompt = (
        f"Create a 7-day detailed workout plan for a person with the goal of '{goal}' "
        f"and intensity level '{intensity}'. Include warm-ups, exercises, sets, reps, "
        f"and rest days in a clear format."
    )

    # Primary model & Fallback models (404 error varamal irukka)
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

    # All API models fail aanaal backup workout plan
    return (
        f"Sample Workout Plan for {goal} ({intensity} intensity):\n\n"
        f"Day 1: Full Body Workout\n"
        f"Day 2: Cardio & Core\n"
        f"Day 3: Active Rest\n"
        f"Day 4: Upper Body\n"
        f"Day 5: Lower Body\n"
        f"Day 6: Light Cardio\n"
        f"Day 7: Rest Day."
    )