from app.application.ports.processor import IDocumentProcessor
from app.application.ports.storage import IStorageService
from app.infrastructure.processor import MockProcessor
from app.infrastructure.storage import MockStorageService


def get_storage_service() -> IStorageService:
    return MockStorageService()


def get_document_processor() -> IDocumentProcessor:
    return MockProcessor()
