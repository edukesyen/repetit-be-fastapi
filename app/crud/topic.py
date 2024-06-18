from sqlalchemy.orm import Session
 
from app import models, schemas
from app.crud.base import CRUDBase
from app import models


class CRUDTopic(CRUDBase):

    def get(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Topic).offset(skip).limit(limit).all()

    def create(self, db: Session, topic: schemas.TopicCreate, user_id: int):
        db_topic = models.Topic(**topic.dict(), user_id=user_id)
        db.add(db_topic)
        db.commit()
        db.refresh(db_topic)
        return db_topic
    

topic = CRUDTopic(models.Topic)