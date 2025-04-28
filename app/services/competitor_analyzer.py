from fastapi import APIRouter, HTTPException
import requests
from typing import List, Dict

router = APIRouter()

@router.get("/competitors/{industry}", response_model=List[Dict[str, str]])
async def analyze_competitors(industry: str):
    params = {
        "engine": "google",
        "q": f"{industry} startup competitors",
        "api_key": "YOUR_SERPAPI_KEY"  # Replace with your actual API key or fetch from environment variables
    }
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        results = response.json()
        competitors = []
        for result in results.get("organic_results", [])[:5]:
            competitors.append({
                "title": result.get("title", "Unknown"),
                "link": result.get("link", "#"),
                "snippet": result.get("snippet", "No description available.")
            })
        return competitors
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))