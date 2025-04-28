from fastapi import FastAPI
from app.api.endpoints import startup

app = FastAPI()

app.include_router(startup.router, prefix="/api/startup", tags=["startup"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gensus Hackathon API"}