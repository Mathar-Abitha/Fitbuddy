import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(title="FitBuddy App")

# Get base directory of 'app'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
IMAGE_PATH = os.path.join(STATIC_DIR, "images", "gym-bg.jpg")

# Debug print to check exact location in terminal
print("--------------------------------------------------")
print("Target Image Path:", IMAGE_PATH)
print("File Exists Status:", os.path.exists(IMAGE_PATH))
print("--------------------------------------------------")

# Mount static files directory
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(router)