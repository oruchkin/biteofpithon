import pydantic
import datetime


class UserBase(pydantic.BaseModel):
    email: str
    name: str
    phone: str


class UserRequest(UserBase):
    password: str


    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
        from_attributes = True


class PostBase(pydantic.BaseModel):
    post_title: str
    post_description: str
    image: str


class PostRequest(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
        from_attributes = True



