from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session


from app import schemas, crud
from sqlalchemy.orm import Session

from app.api.deps import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Flashcard)
def create_flashcard_for_user(
    topic_id: int, 
    flashcard: schemas.FlashcardCreate, 
    db: Session = Depends(get_db)
):
    return crud.flashcard.create(db=db, flashcard=flashcard, topic_id=topic_id)


@router.get("/", response_model=list[schemas.Flashcard])
def read_flashcards(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    print(skip)
    flashcards = crud.flashcard.get(db, skip=skip, limit=limit)
    return flashcards