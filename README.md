# Gensus Hackathon Backend

## Overview
The Gensus Hackathon Backend is a FastAPI application designed to assist startup founders by providing tools for idea refinement, business plan generation, pitch deck creation, competitor analysis, and city industry growth insights.

## Project Structure
```
gensus-hackathon-backend
├── app
│   ├── main.py                     # Entry point for the FastAPI application
│   ├── api
│   │   ├── endpoints
│   │   │   └── startup.py          # API endpoints for startup functionalities
│   │   └── __init__.py             # Initializes the API module
│   ├── core
│   │   ├── config.py               # Configuration settings for the application
│   │   └── __init__.py             # Initializes the core module
│   ├── models
│   │   └── __init__.py             # Initializes the models module
│   ├── services
│   │   ├── idea_assistant.py        # Logic for assisting with startup ideas
│   │   ├── business_plan_generator.py # Logic for generating business plans
│   │   ├── pitch_deck_writer.py     # Logic for creating pitch deck content
│   │   ├── competitor_analyzer.py    # Logic for analyzing competitors
│   │   └── city_industry_growth.py   # Logic for analyzing startup growth trends
│   └── __init__.py                  # Initializes the app module
├── requirements.txt                 # Lists project dependencies
├── README.md                        # Documentation for the project
└── .env                             # Environment variables for the application
```

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd gensus-hackathon-backend
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add your environment variables, such as API keys and configuration settings.

5. **Run the Application**
   ```
   uvicorn app.main:app --reload
   ```

## Usage
- Access the API documentation at `http://127.0.0.1:8000/docs` after running the application.
- Use the endpoints defined in `app/api/endpoints/startup.py` to interact with the application functionalities.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.