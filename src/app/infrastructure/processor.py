from typing import Any, BinaryIO
from app.application.ports.processor import IDocumentProcessor


class MockProcessor(IDocumentProcessor):
    def process(self, document: BinaryIO) -> Any:
        print("Processed")
