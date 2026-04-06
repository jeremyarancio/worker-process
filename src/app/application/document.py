from uuid import uuid4

from app.application.ports.storage import IStorageService
from app.application.ports.worker import IWorkerService
from app.domain.document import DocumentId
from app.domain.worker import JobId
from app.application.workers import tasks


class DocumentService:
    @staticmethod
    def generate_presigned_url(storage_service: IStorageService) -> str:
        document_id = DocumentId(uuid4())
        presigned_url = storage_service.generate_presigned_url(document_id=document_id)
        return presigned_url

    @staticmethod
    def process(
        document_id: DocumentId,
        worker_service: IWorkerService,
    ) -> JobId:
        job_id = worker_service.enqueue(tasks.process_document, document_id)
        return job_id

    @staticmethod
    def get_presigned_url(
        document_id: DocumentId, storage_service: IStorageService
    ) -> str:
        return storage_service.get_presigned_url(document_id=document_id)
