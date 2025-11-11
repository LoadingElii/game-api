import math
import nflreadpy as nfl
from datetime import datetime
import polars as pl

from app.core.cache import set_cache, get_cache


def get_games_by_week():
    season = datetime.today().year
    week = nfl.get_current_week()

    df = nfl.load_schedules([season])
    week_games = df.filter(pl.col("week") == week)

    if week_games.is_empty():
        return []

    cols = ["game_id", "week", "season", "home_team",
            "away_team", "home_score", "away_score", "gameday"]

    week_games = week_games.select(cols)

    games = []
    for row in week_games.iter_rows(named=True):
        games.append({
            "game_id": row["game_id"],
            "week": row["week"],
            "season": row["season"],
            "home_team": row["home_team"],
            "away_team": row["away_team"],
            "home_score": row["home_score"],
            "away_score": row["away_score"],
            "gameday": row["gameday"]
        })

    return games


async def update_game_cache():
    games = get_games_by_week()
    await set_cache("games", games, expire_seconds=86400)
    return games


async def get_games_from_cache():
    games = await get_cache("games")
    if not games:
        return update_game_cache()
    return games
