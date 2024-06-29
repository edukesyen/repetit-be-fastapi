from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    user = relationship("User", back_populates="topics")
    flashcards = relationship("Flashcard", back_populates="topic")