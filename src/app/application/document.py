from uuid import uuid4

from app.application.ports.storage import IStorageService
from app.application.ports.worker import IWorkerService
from app.domain.document import DocumentId
from app.domain.worker import JobId


class DocumentService:
    @staticmethod
    def generate_presigned_url(storage_service: IStorageService) -> str:
        document_id = DocumentId(uuid4())
        presigned_url = storage_service.generate_presigned_url(document_id=document_id)
        return presigned_url

    @classmethod
    def process(
        cls,
        document_id: DocumentId,
        storage_service: IStorageService,
        worker_service: IWorkerService,
    ) -> JobId:
        job_id = worker_service.enqueue(cls._process_task, document_id, storage_service)
        return job_id

    @staticmethod
    def _process_task(
        document_id: DocumentId, storage_service: IStorageService
    ) -> None:
        print(f"Processing document {document_id}")
        # TODO: Add actual document processing logic

    @staticmethod
    def check_job(job_id: JobId, worker_service: IWorkerService):
        return worker_service.check(job_id=job_id)

    @staticmethod
    def get_presigned_url(
        document_id: DocumentId, storage_service: IStorageService
    ) -> str:
        return storage_service.get_presigned_url(document_id=document_id)
