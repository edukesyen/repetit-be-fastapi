from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=True)

    topic = relationship("Topic", back_populates="flashcards")