from pydantic import (BaseModel, EmailStr, validator,
                      ValidationError, Field, root_validator)
from app.libs.default_factories import current_time, generate_uuid

from datetime import datetime

from typing import Optional


class ProvinsiBase(BaseModel):
    class Config:
        validate_assignment = True


class MemberCreate(ProvinsiBase):
    id: int
    code: str
    name: str
    updated_at: datetime = Field(default_factory=current_time)
    created_at: datetime = Field(default_factory=current_time)
    is_penalized: bool = False


class MemberUpdate(ProvinsiBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__fields_set__.add('updated_at')

    name: Optional[str]
    updated_at: datetime = Field(default_factory=current_time)
    is_penalized: Optional[bool]


class MemberSearch(BaseModel):
    name_like: Optional[str]
    is_penalized: Optional[bool]
