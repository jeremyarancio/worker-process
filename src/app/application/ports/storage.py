from abc import ABC, abstractmethod

from app.domain.document import DocumentId


class IStorageService(ABC):
    @abstractmethod
    def generate_presigned_url(self, document_id: DocumentId): ...
