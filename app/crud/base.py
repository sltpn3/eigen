from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union, Tuple

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query

from app.db.base_class import Base
import re

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self,
        db: Session, *,
        query: Union[Query, None] = None,
        skip: int = 0,
        limit: int = 100,
        filters: Union[dict, None] = None,
        orders: Union[List[str], None] = None,
        columns: Union[List[str], None] = None
    ) -> Tuple[List[ModelType], int]:
        if not query:
            if not columns:
                query = db.query(self.model)
                # print(type(query))
            else:
                column_args = []
                for column in columns:
                    column_args.append(getattr(self.model, column))
                query = db.query(*column_args)
        if filters:
            filter_args = []
            for attr, value in filters.items():
                if re.search("_like$", attr):
                    if value:
                        filter_args.append(getattr(self.model, attr.replace(
                            '_like', '')).like('%{}%'.format(value)))
                else:
                    filter_args.append(getattr(self.model, attr) == value)
            query = query.filter(*filter_args)
        if orders:
            order_args = []
            for order in orders:
                attr, sort = order.split(' ')
                if sort.lower() == 'desc':
                    order_args.append(getattr(self.model, attr).desc())
                elif sort.lower() == 'asc':
                    order_args.append(getattr(self.model, attr).asc())
            query = query.order_by(*order_args)
        count = query.count()
        query = query.offset(skip).limit(limit)
        return (query.all(), count)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
