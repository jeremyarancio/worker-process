import os

from fastapi import Depends
from redis import Redis

from app.application.ports.worker import IWorkerService

from app.application.ports.storage import IStorageService
from app.infrastructure.storage import LocalStorageService
from app.infrastructure.worker import RQWorkerService


def get_storage_service() -> IStorageService:
    return LocalStorageService(base_dir="/tmp/storage")


def get_redis_conn():
    return Redis(
        host=os.environ.get("REDIS_HOST", "localhost"),
        port=int(os.environ.get("REDIS_PORT", "6379")),
    )


def get_worker_service(redis_conn=Depends(get_redis_conn)) -> IWorkerService:
    return RQWorkerService(redis_conn=redis_conn)
