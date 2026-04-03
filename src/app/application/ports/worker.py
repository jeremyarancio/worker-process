from abc import ABC, abstractmethod
from typing import Callable

from app.domain.worker import JobId, Status


class IWorkerService(ABC):
    @abstractmethod
    def enqueue(self, task: Callable, *params) -> JobId: ...

    @abstractmethod
    def check(self, job_id: JobId) -> Status: ...
