from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class PitchDeckSlide(BaseModel):
    slide: str
    content: str

class PitchDeckRequest(BaseModel):
    refined_idea: str
    business_plan: Dict

class PitchDeckResponse(BaseModel):
    slides: List[PitchDeckSlide]

@router.post("/pitch-deck", response_model=PitchDeckResponse)
async def create_pitch_deck(request: PitchDeckRequest):
    # Logic to generate pitch deck slides based on the business plan
    slides = [
        {"slide": "Problem", "content": f"Problem related to {request.refined_idea}."},
        {"slide": "Solution", "content": f"Solution for {request.refined_idea}."},
        {"slide": "Market", "content": "Market analysis content."},
        {"slide": "Team", "content": "Team information."},
        {"slide": "Ask", "content": "Funding request details."}
    ]
    
    return PitchDeckResponse(slides=slides)