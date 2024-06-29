from sqlalchemy.orm import Session
 
from app import models, schemas
from app.crud.base import CRUDBase
from app import models


class CRUDFlashcard(CRUDBase):

    def get(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Flashcard).offset(skip).limit(limit).all()

    def create(self, db: Session, flashcard: schemas.FlashcardCreate, topic_id: int):
        db_flashcard = models.Flashcard(**flashcard.dict(), topic_id=topic_id)
        db.add(db_flashcard)
        db.commit()
        db.refresh(db_flashcard)
        return db_flashcard
    

topic = CRUDFlashcard(models.Flashcard)