from fastapi import FastAPI
from app.routers import game_router, prediction_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
    description="API for retrieving NFL game data using nflreadpy.",
)

app.include_router(game_router.router)
app.include_router(prediction_router.router)

@app.get("/")
def root():
    return {
        "message": f"{settings.app_name}!",
        "version": settings.version,
    }
