from typing import Annotated
from fastapi import APIRouter, Depends
from uuid import UUID

from app.application.document import DocumentService
from app.application.ports.storage import IStorageService
from app.application.ports.worker import IWorkerService
from app.domain.worker import JobId, Status
from app.interface.dependencies import get_storage_service, get_worker_service
from app.domain.document import DocumentId

router = APIRouter(prefix="/documents", tags=["document"])


@router.get("/upload")
def upload(
    storage_service: Annotated[IStorageService, Depends(get_storage_service)],
) -> str:
    presigned_url = DocumentService.generate_presigned_url(
        storage_service=storage_service
    )
    return presigned_url


@router.post("/{document_id}/uploaded")
def uploaded(
    document_id: UUID,
    worker_service: Annotated[IWorkerService, Depends(get_worker_service)],
    storage_service: Annotated[IStorageService, Depends(get_storage_service)],
) -> JobId:
    job_id = DocumentService.process(
        document_id=DocumentId(document_id),
        worker_service=worker_service,
        storage_service=storage_service,
    )
    return job_id


@router.get("/status/{job_id}")
def check_job(
    job_id: str,
    worker_service: Annotated[IWorkerService, Depends(get_worker_service)],
) -> Status:
    status = DocumentService.check_job(
        job_id=JobId(job_id),
        worker_service=worker_service,
    )
    return status


@router.get("/download/{document_id}")
def download(
    document_id: UUID,
    storage_service: Annotated[IStorageService, Depends(get_storage_service)],
) -> str:
    presigned_url = DocumentService.get_presigned_url(
        document_id=DocumentId(document_id), storage_service=storage_service
    )
    return presigned_url
