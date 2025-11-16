from pydantic import BaseModel


class PredictionSchema(BaseModel):
    game_id: str
    home_team: str
    away_team: str
    home_win_probability: float
    away_win_probability: float