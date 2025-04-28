from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import json
import pandas as pd
import serpapi

router = APIRouter()

SERPAPI_KEY = "your_serpapi_key_here"

@router.post("/city-industry-growth")
async def fetch_city_industry_growth(city: str, industry: str) -> Dict[str, Any]:
    params = {
        "engine": "google",
        "q": f"{industry} startups {city} growth trends 2023..2025",
        "api_key": SERPAPI_KEY
    }
    try:
        results = serpapi.search(params)
        startups = []
        for result in results.get("organic_results", [])[:5]:
            startups.append({
                "name": result.get("title", "Unknown Startup"),
                "description": result.get("snippet", "No description available."),
                "website": result.get("link", "#")
            })
        
        analysis = analyze_growth(startups, industry, city)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def analyze_growth(startups: list, industry: str, city: str) -> Dict[str, Any]:
    # Placeholder for growth analysis logic
    growing_count = sum(1 for startup in startups if "growing" in startup.get("description", "").lower())
    struggling_count = sum(1 for startup in startups if "struggling" in startup.get("description", "").lower())
    total = growing_count + struggling_count

    stats = {
        "growing_percentage": (growing_count / total * 100) if total > 0 else 50.0,
        "struggling_percentage": (struggling_count / total * 100) if total > 0 else 50.0
    }

    return {"analysis": startups, "stats": stats}