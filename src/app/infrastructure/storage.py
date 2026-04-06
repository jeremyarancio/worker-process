from io import BytesIO
from pathlib import Path
from typing import BinaryIO

import boto3

from app.application.ports.storage import IStorageService
from app.domain.document import DocumentId


class LocalStorageService(IStorageService):
    def __init__(
        self,
        base_dir: str,
        unprocessed_folder: str = "unprocessed",
        processed_folder: str = "processed",
    ) -> None:
        self._base_dir = Path(base_dir)
        self._unprocessed_dir = self._base_dir / unprocessed_folder
        self._processed_dir = self._base_dir / processed_folder
        self._unprocessed_dir.mkdir(parents=True, exist_ok=True)
        self._processed_dir.mkdir(parents=True, exist_ok=True)

    def generate_presigned_url(self, document_id: DocumentId) -> str:
        return str(self._unprocessed_dir / str(document_id))

    def get_presigned_url(self, document_id: DocumentId) -> str:
        return str(self._unprocessed_dir / str(document_id))

    def store_processed_document(self, obj: BinaryIO, document_id: DocumentId) -> None:
        path = self._processed_dir / str(document_id)
        with open(path, "wb") as f:
            f.write(obj.read())

    def get_unprocessed_document(self, document_id: DocumentId) -> BinaryIO:
        path = self._unprocessed_dir / str(document_id)
        return BytesIO(path.read_bytes())


class S3StorageService(IStorageService):
    def __init__(
        self,
        bucket: str,
        unprocessed_folder: str,
        processed_folder: str,
    ) -> None:
        self._client = boto3.client("s3")
        self._bucket = bucket
        self._unprocessed_folder = unprocessed_folder
        self._processed_folder = processed_folder

    def generate_presigned_url(self, document_id: DocumentId) -> str:
        return self._client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": self._bucket,
                "Key": f"{self._unprocessed_folder}/{document_id}",
            },
            ExpiresIn=900,
        )

    def get_presigned_url(self, document_id: DocumentId) -> str:
        return self._client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": self._bucket,
                "Key": f"{self._unprocessed_folder}/{document_id}",
            },
            ExpiresIn=900,
        )

    def store_processed_document(self, obj: BinaryIO, document_id: DocumentId) -> None:
        self._client.upload_fileobj(
            obj,
            self._bucket,
            f"{self._processed_folder}/{document_id}",
        )

    def get_unprocessed_document(self, document_id: DocumentId) -> BinaryIO:
        response = self._client.get_object(
            Bucket=self._bucket,
            Key=f"{self._unprocessed_folder}/{document_id}",
        )
        return response["Body"]
