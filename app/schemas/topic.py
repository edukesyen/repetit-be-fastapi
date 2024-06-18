from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str


class TopicCreate(TopicBase):
    pass


class Topic(TopicBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True