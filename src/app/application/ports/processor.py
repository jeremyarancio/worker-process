from abc import ABC, abstractmethod
from typing import Any, BinaryIO


class IDocumentProcessor(ABC):
    @abstractmethod
    def process(self, document: BinaryIO) -> Any: ...
