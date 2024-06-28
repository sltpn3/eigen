import typing as t
import re

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import MetaData

class_registry: t.Dict = {}

meta = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})


@as_declarative(class_registry=class_registry, metadata=meta)
class Base:
    id: t.Any
    __name__: str
    # metadata = meta

    # @declared_attr
    # def metadata(cls):
    #     return meta

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        '''CamelCase to snake_case'''
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', cls.__name__)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()