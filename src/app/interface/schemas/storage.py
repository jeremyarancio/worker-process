from pydantic import BaseModel


class PresignedUrlResponse(BaseModel):
    url: str
