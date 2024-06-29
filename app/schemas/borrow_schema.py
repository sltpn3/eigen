from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Table, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

'''Relationship Schemas between jaringan_relawan dan wilayah'''


class Borrow(Base):
    book_id = Column(Integer, ForeignKey(
        'book.id'), primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey(
        'member.id'), primary_key=True, index=True)
    date = Column(Date, nullable=False)
    is_returned = Column(Boolean, default=False)
