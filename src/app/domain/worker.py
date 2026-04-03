from enum import StrEnum
from typing import NewType


JobId = NewType("JobId", str)


class Status(StrEnum):
    DONE = "DONE"
    FAILED = "FAILED"
    STARTED = "STARTED"
    QUEUED = "QUEUED"
