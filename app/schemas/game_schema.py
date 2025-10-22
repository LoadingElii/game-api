import math
from typing import Optional

from pydantic import BaseModel, field_validator
from datetime import date

class GameSchema(BaseModel):
    game_id: str
    week: int
    season: int
    home_team: str
    away_team: str
    home_score: Optional[int]
    away_score: Optional[int]
    gameday: date

    @field_validator("home_score", "away_score", mode="before")
    def nan_to_zero(cls, v):
        # if it's a float and is NaN or infinite, convert to 0
        if isinstance(v, float):
            if math.isnan(v) or not math.isfinite(v):
                return 0
        # If it's None or missing, you may also want to map that:
        if v is None:
            return 0
        # Otherwise leave it (or coerce to int if needed):
        try:
            return int(v)
        except (ValueError, TypeError):
            # fallback default
            return 0