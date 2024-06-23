from typing import Optional

from pydantic import BaseModel, HttpUrl, field_validator


class CreateURLRequest(BaseModel):
    long_url: HttpUrl
    custom_slug: Optional[str] = None

    @field_validator('custom_slug')
    def custom_slug_must_be_valid(cls, v):
        if v:
            if not v.isalnum() or len(v) > 20:
                raise ValueError(
                    'Custom slug must be alphanumeric and no longer than 20 characters')
        return v

class ShortURLCreated(BaseModel):
    long_url: HttpUrl
    short_url: HttpUrl


class CreateURLResponse(BaseModel):
    message: str
    status_code: int
    short: ShortURLCreated
