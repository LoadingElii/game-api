from fastapi import APIRouter, HTTPException

from app.schemas.prediction_schema import PredictionSchema
from app.services.prediction_service import win_prediction_for_game

router = APIRouter(prefix="/predictions", tags=["predictions"])

@router.get("/winprobability/{home_team}/{away_team}", response_model=PredictionSchema)
def get_prediction_for_game(home_team: str, away_team: str):
    prediction = win_prediction_for_game(home_team, away_team)
    if not prediction:
        raise HTTPException(status_code=404, detail="No predictions found")
    return prediction