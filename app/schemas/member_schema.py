from sqlalchemy import (Integer, String, Column, Boolean,
                        DateTime, Text, Float, Date)
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship

from app.db.base_class import Base

'''DB Schema provinsi'''


class Member(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(16), nullable=False, unique=True)
    name = Column(String(256), nullable=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    penalized_until = Column(Date, nullable=True)
