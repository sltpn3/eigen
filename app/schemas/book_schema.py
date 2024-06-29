from sqlalchemy import (Integer, String, Column, Boolean,
                        DateTime, Text, Float, Date)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
# from app.schemas.borrow_schema import association_table

from app.db.base_class import Base

'''DB Schema provinsi'''


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(16), nullable=False, unique=True)
    title = Column(String(256), nullable=False)
    author = Column(String(256), nullable=False)
    amount = Column(Integer)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

    available = None

    # Relationship
    borrowed_by = relationship(
        "Borrow",
        primaryjoin='and_(Borrow.book_id==Book.id, Borrow.is_returned==0)'
        # secondary=association_table
    )
