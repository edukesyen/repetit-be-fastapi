from sqlalchemy import Boolean, Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.utils.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole)) # "STUDENT" or "MENTOR"

    topics = relationship("Topic", back_populates="user")