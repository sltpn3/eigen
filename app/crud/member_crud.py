from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.models.member_model import MemberCreate, MemberUpdate
from app.schemas.member_schema import Member

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from typing import Any, Dict, Optional, Union, TypeVar, List, Tuple

ModelType = TypeVar("ModelType", bound=Base)


class CRUDMember(CRUDBase[Member, MemberCreate, MemberUpdate]):
    def get_by_code(self, db: Session, code: str) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.code == code).first()


member = CRUDMember(Member)
