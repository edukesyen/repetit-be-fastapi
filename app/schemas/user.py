from pydantic import BaseModel
from app.schemas.topic import Topic
from app.utils.enums import UserRole

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    nickname: str
    full_name: str
    role: UserRole
    password: str


class User(UserBase):
    id: int
    is_active: bool
    topics: list[Topic] = []

    class Config:
        orm_mode = True