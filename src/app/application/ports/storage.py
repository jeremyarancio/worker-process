from abc import ABC, abstractmethod

from app.domain.document import DocumentId
from typing import BinaryIO


class IStorageService(ABC):
    @abstractmethod
    def generate_presigned_url(self, document_id: DocumentId) -> str: ...

    @abstractmethod
    def get_presigned_url(self, document_id: DocumentId) -> str: ...

    @abstractmethod
    def store_processed_document(
        self, obj: BinaryIO, document_id: DocumentId
    ) -> None: ...

    @abstractmethod
    def get_unprocessed_document(self, document_id: DocumentId) -> BinaryIO: ...
