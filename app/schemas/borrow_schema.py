from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Table, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.schemas.book_schema import Book

'''Relationship Schemas between jaringan_relawan dan wilayah'''


class Borrow(Base):
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey(
        'book.id'), index=True)
    member_id = Column(Integer, ForeignKey(
        'member.id'), index=True)
    date = Column(Date, nullable=False)
    is_returned = Column(Boolean, default=False)

    # Relationship
    book = relationship('Book')
    member = relationship('Member')
