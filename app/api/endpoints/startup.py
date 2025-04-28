from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.services.idea_assistant import idea_assistant
from app.services.business_plan_generator import business_plan_generator
from app.services.pitch_deck_writer import pitch_deck_writer
from app.services.competitor_analyzer import competitor_analyzer
from app.services.city_industry_growth import fetch_city_industry_growth

router = APIRouter()

@router.post("/startup/idea", response_model=Dict)
async def generate_startup_idea(industry: str, idea: str):
    state = {
        "idea": idea,
        "industry": industry,
        "refined_idea": "",
        "market_gap": "",
        "business_plan": {},
        "pitch_deck": [],
        "competitors": []
    }
    return await idea_assistant(state)

@router.post("/startup/business-plan", response_model=Dict)
async def generate_business_plan(refined_idea: str, industry: str, market_gap: str):
    state = {
        "refined_idea": refined_idea,
        "industry": industry,
        "market_gap": market_gap,
        "business_plan": {},
        "pitch_deck": [],
        "competitors": []
    }
    return await business_plan_generator(state)

@router.post("/startup/pitch-deck", response_model=Dict)
async def generate_pitch_deck(refined_idea: str, business_plan: Dict):
    state = {
        "refined_idea": refined_idea,
        "business_plan": business_plan,
        "pitch_deck": []
    }
    return await pitch_deck_writer(state)

@router.get("/startup/competitors", response_model=List[Dict])
async def analyze_competitors(industry: str):
    state = {
        "industry": industry,
        "competitors": []
    }
    return await competitor_analyzer(state)

@router.post("/startup/city-growth", response_model=Dict)
async def analyze_city_growth(city: str, industry: str):
    return await fetch_city_industry_growth(city, industry)