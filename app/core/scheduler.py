import logging
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.core.cache import set_cache
from app.services.game_service import update_game_cache
from app.services.prediction_service import win_prediction_for_game

scheduler = AsyncIOScheduler(timezone="America/Chicago")


async def refresh_caches():
    logging.info(f"Refreshing cache at {datetime.now()}")

    #refresh game cache
    games = await update_game_cache()

    #refresh prediction cache
    for game in games:
        prediction = await win_prediction_for_game(game["home_team"], game["away_team"])
        cache_key = f"{game['home_team']}/{game['away_team']}"
        await set_cache(cache_key, prediction.model_dump(), expire_seconds=86400)
    logging.info(f"Cache refresh complete")

def start_scheduler():
    scheduler.add_job(refresh_caches, "cron", hour=22, minute=0)
    scheduler.start()
    logging.info("Scheduler started..refresh at 10pm daily")
