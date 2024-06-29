from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.models.book_model import BookCreate, BookUpdate
from app.schemas.book_schema import Book

from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from typing import Any, Dict, Optional, Union, TypeVar, List, Tuple

ModelType = TypeVar("ModelType", bound=Base)


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def get_by_code(self, db: Session, code: str) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.code == code).first()


book = CRUDBook(Book)
