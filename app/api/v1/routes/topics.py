from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session


from app import schemas, crud
from sqlalchemy.orm import Session

from app.api.deps import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Topic)
def create_topic_for_user(
    user_id: int, 
    topic: schemas.TopicCreate, 
    db: Session = Depends(get_db)
):
    return crud.topic.create(db=db, topic=topic, user_id=user_id)


@router.get("/", response_model=list[schemas.Topic])
def read_topics(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    print(skip)
    topics = crud.topic.get(db, skip=skip, limit=limit)
    return topics