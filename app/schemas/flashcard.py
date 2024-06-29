from datetime import date
from pydantic import BaseModel


class FlashcardBase(BaseModel):
    question: str
    due_date: date


class FlashcardCreate(FlashcardBase):
    pass


class Flashcard(FlashcardBase):
    id: int
    topic_id: int

    class Config:
        orm_mode = True