# from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from sqlalchemy.orm import Session


# class CRUDBase():
#     def __init__(self):
#         """
#         CRUD object with default methods to Create, Read, Update, Delete (CRUD).

#         **Parameters**

#         * `model`: A SQLAlchemy model class
#         * `schema`: A Pydantic model (schema) class
#         """
#         pass

from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
