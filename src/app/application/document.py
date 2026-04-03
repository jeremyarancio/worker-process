from uuid import uuid4
from app.domain.document import DocumentId


class DocumentService:
    @staticmethod
    def upload(storage_service: IStorageService):
        document_id = DocumentId(uuid4())
        storage_service
