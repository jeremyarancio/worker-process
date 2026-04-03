import os

from redis import Redis
from rq import Queue


redis_conn = Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
)

queue = Queue(connection=redis_conn)
