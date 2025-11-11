from fastapi import APIRouter

from app.core.scheduler import refresh_caches

router = APIRouter(prefix="/cache", tags=["cache"])

@router.post("/refresh")
async def refresh_cache():
    await refresh_caches()
    return {"message": "Cache refreshed"}