from sqlalchemy import Integer, String, Column, Boolean, DateTime, ForeignKey, Table, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

'''Relationship Schemas between jaringan_relawan dan wilayah'''

association_table = Table('borrow', Base.metadata,
                          Column('member_id', ForeignKey(
                              'member.id'), primary_key=True),
                          Column('book_id', ForeignKey(
                              'book.id'), primary_key=True),
                          Column('borrow_date', Date, nullable=False),
                          Column('is_returned', Boolean, default=False))
