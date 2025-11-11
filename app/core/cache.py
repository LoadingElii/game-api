import redis
import json
from app.core.config import settings

r = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, decode_responses=True)


def set_cache(key: str, value, expire_seconds: int | None):
    r.set(key, json.dumps(value), ex=expire_seconds)

def get_cache(key: str):
    value = r.get(key)
    if value:
      return json.loads(value)
    return None