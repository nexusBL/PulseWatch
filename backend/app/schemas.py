from pydantic import BaseModel, HttpUrl
from datetime import datetime


class URLCreate(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    id: int
    url: str
    created_at: datetime

    class Config:
        from_attributes = True

class StatusResponse(BaseModel):
    id: int
    url: str
    status_code: int | None
    response_time: float | None
    is_up: bool
    checked_at: datetime | None      