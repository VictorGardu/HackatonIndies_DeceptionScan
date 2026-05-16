import requests
import os
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")


def analyze_event(event):

    prompt = f"""
You are a cybersecurity deception engine.

Return ONLY valid JSON.

Format:
{{
  "classification":"reconnaissance",
  "threat_level":"medium",
  "recommended_profile":"legacy_linux"
}}

Event:
{event}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "temperature": 0.2,
            "max_tokens": 300,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    result = response.json()

    print(result)

    content = result["choices"][0]["message"]["content"]

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print(content)

    return json.loads(content)
