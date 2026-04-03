from typing import Annotated
from fastapi import Depends, FastAPI

from app.application.document import DocumentService
from app.interface.schemas.storage import PresignedUrlResponse

app = FastAPI()


@app.get("")
def welcome():
    return "Welcome to the worker processing demo!"


@app.get("/upload")
def upload(
    storage_service: Annotated[IStorageService, Depends(get_storage_service)],
) -> PresignedUrlResponse:
    presigned_url = DocumentService.upload(storage_service=storage_service)
    return PresignedUrlResponse(url=presigned_url)
