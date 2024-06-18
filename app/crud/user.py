from sqlalchemy.orm import Session
 
from app import models, schemas
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase):
    def get_by_id(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_by_email(db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    def create(db: Session, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
user = CRUDUser()