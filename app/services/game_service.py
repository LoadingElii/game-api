import math

import nflreadpy as nfl
from datetime import datetime
import polars as pl

def get_games_by_week():
    season = datetime.today().year
    week = nfl.get_current_week()

    df = nfl.load_schedules([season])
    week_games = df.filter(pl.col("week") == week)

    if week_games.is_empty():
        return []

    cols = ["game_id", "week", "season","home_team",
            "away_team", "home_score", "away_score", "gameday" ]

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


