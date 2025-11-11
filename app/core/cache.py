from redis import asyncio as aioredis
import json
from app.core.config import settings

redis_client: aioredis.Redis | None = None

async def init_redis():
    global redis_client
    redis_client = aioredis.from_url(f"redis://{settings.redis_host}:{settings.redis_port}",
                                     decode_responses=True)
    try:
        await redis_client.ping()
        print("Redis connection established")
    except Exception as e:
        print(f"Redis connection failed: {e}")

async def set_cache(key: str, value, expire_seconds: int | None):
    if not redis_client:
        return
    await redis_client.set(key, json.dumps(value), ex=expire_seconds)

async def get_cache(key: str):
    if not redis_client:
        return None
    value = await redis_client.get(key)
    if value:
      return json.loads(value)
    return None

async def delete_cache(key: str):
    if redis_client:
        await redis_client.delete(key)