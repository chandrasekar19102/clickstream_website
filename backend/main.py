from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import psycopg2

app = FastAPI()


# Define Event Schema
class ClickEvent(BaseModel):
    category: str
    action: str
    label: str
    url: str
    timestamp: str

@app.post("/track")
def track_event(event: ClickEvent):

    print("Inside track post method")
    return {
        "Name" : "ClickEvent.category"
    }

# Serve Frontend

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")