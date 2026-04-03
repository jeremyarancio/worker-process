from typing import Callable

from redis import Redis
from rq import Queue
from rq.job import Job

from loguru import logger

from app.application.ports.worker import IWorkerService
from app.domain.worker import JobId, Status


STATUS_MAP = {
    "failed": Status.FAILED,
    "queued": Status.QUEUED,
    "started": Status.STARTED,
    "finished": Status.DONE,
}


class RQWorkerService(IWorkerService):
    def __init__(self, redis_conn: Redis):
        self.redis_conn = redis_conn
        self.queue = Queue(connection=redis_conn)

    def enqueue(self, task: Callable, *params) -> JobId:
        job = self.queue.enqueue(task, *params)
        return JobId(job.id)

    def check(self, job_id: JobId) -> Status:
        job = Job.fetch(id=job_id, connection=self.redis_conn)
        rq_status = job.get_status(refresh=True)
        status = STATUS_MAP.get(rq_status)
        if status:
            return status
        logger.error("Job status not handled correctly: {}", rq_status)
        raise Exception
