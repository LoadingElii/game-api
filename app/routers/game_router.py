from fastapi import APIRouter, HTTPException
from app.schemas.game_schema import GameSchema
from app.services.game_service import get_games_from_cache

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/currentweek", response_model=list[GameSchema])
async def get_games_for_week():
    games = await get_games_from_cache()
    if not games:
        raise HTTPException(status_code=404, detail="No games found")
    return games
