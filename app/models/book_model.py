from pydantic import (BaseModel, EmailStr, validator,
                      ValidationError, Field, root_validator)
from app.libs.default_factories import current_time, generate_uuid

from datetime import datetime

from typing import Optional


class BookBase(BaseModel):
    class Config:
        validate_assignment = True


class BookCreate(BookBase):
    id: int
    code: str
    title: str
    author: str
    amount: int
    updated_at: datetime = Field(default_factory=current_time)
    created_at: datetime = Field(default_factory=current_time)


class BookUpdate(BookBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.model_fields_set.add('updated_at')

    name: Optional[str]
    updated_at: datetime = Field(default_factory=current_time)


class BookSearch(BaseModel):
    title_like: Optional[str] = None
    author_like: Optional[str] = None
