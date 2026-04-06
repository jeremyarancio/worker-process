from typing import Any, BinaryIO
import time

from app.application.ports.processor import IDocumentProcessor


class MockProcessor(IDocumentProcessor):
    def process(self, document: BinaryIO) -> Any:
        time.sleep(30)
        print("Processed")
