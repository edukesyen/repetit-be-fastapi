# from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from sqlalchemy.orm import Session


class CRUDBase():
    def __init__(self):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        pass