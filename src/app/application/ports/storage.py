from abc import ABC, abstractmethod

from app.domain.document import DocumentId
from typing import BinaryIO


class IStorageService(ABC):
    @abstractmethod
    def generate_presigned_url(self, document_id: DocumentId) -> str: ...

    @abstractmethod
    def get_presigned_url(self, document_id: DocumentId) -> str: ...

    @abstractmethod
    def store_document(self, obj: BinaryIO) -> None: ...

    @abstractmethod
    def get_document(self, document_id: DocumentId) -> BinaryIO: ...
