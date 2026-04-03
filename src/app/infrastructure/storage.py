from typing import BinaryIO
from app.application.ports.storage import IStorageService
from app.domain.document import DocumentId


class MockStorageService(IStorageService):
    def generate_presigned_url(self, document_id: DocumentId) -> str:
        return f"mocked_presigned_url/{document_id}"

    def get_presigned_url(self, document_id: DocumentId) -> str:
        return f"mocked_presigned_url/{document_id}"

    def store_document(self, obj: BinaryIO) -> None:
        print("Document stored.")

    def get_document(self, document_id: DocumentId) -> BinaryIO:
        return b"Document"


# class S3StorageService(IStorageService):
#     def __init__(self, client: S3Client, bucket: str) -> None:
#         self._client = client
#         self._bucket = bucket
#
#     def generate_presigned_url(self, document_id: DocumentId) -> str:
#         return self._client.generate_presigned_url(
#             "put_object",
#             Params={
#                 "Bucket": self._bucket,
#                 "Key": f"documents/{document_id}",
#             },
#             ExpiresIn=3600,
#         )
