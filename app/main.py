from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.cache import init_redis, redis_client
from app.core.scheduler import start_scheduler, scheduler
from app.routers import game_router, prediction_router, cache_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_redis()
    start_scheduler()
    print("App started")
    yield
    scheduler.shutdown()
    if redis_client:
        await redis_client.close()
    print("App shutdown")


app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    description="API for retrieving NFL game data using nflreadpy.",
    lifespan= lifespan,
)

app.include_router(game_router.router)
app.include_router(prediction_router.router)
app.include_router(cache_router.router)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name}!",
        "version": settings.version,
    }

