from fastapi import FastAPI
from pydantic import BaseModel

from services.openrouter import analyze_event

app = FastAPI()

class ScanEvent(BaseModel):
    source_ip: str
    ports: list[int]
    request_count: int
    detected_tools: list[str]

@app.get("/")
async def root():
    return {"status": "AI Engine Running"}

@app.post("/analyze")
async def analyze(event: ScanEvent):

    ai_response = analyze_event(event.dict())

    return ai_response
