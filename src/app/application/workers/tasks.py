from app.application.ports.processor import IDocumentProcessor
from app.application.ports.storage import IStorageService
from app.application.workers.dependencies import (
    get_document_processor,
    get_storage_service,
)
from app.domain.document import DocumentId


def process_document(
    document_id: DocumentId,
    storage_service: IStorageService = get_storage_service(),
    document_processor: IDocumentProcessor = get_document_processor(),
) -> None:
    print(f"Processing document {document_id}")
    document_bytes = storage_service.get_unprocessed_document(document_id=document_id)
    result = document_processor.process(document=document_bytes)
    storage_service.store_processed_document(obj=result, document_id=document_id)
