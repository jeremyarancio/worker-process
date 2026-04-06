from app.application.ports.processor import IDocumentProcessor
from app.application.ports.storage import IStorageService
from app.infrastructure.processor import MockProcessor
from app.infrastructure.storage import LocalStorageService


def get_storage_service() -> IStorageService:
    return LocalStorageService(base_dir="/tmp/storage")


def get_document_processor() -> IDocumentProcessor:
    return MockProcessor()
