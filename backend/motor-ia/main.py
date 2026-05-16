from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScanEvent(BaseModel):
    source_ip: str
    ports: list[int]
    request_count: int
    detected_tools: list[str]

@app.post("/analyze")
async def analyze(event: ScanEvent):

    return {
        "classification": "reconnaissance",
        "threat_level": "medium",
        "recommended_profile": "legacy_linux"
    }
