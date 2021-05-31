from fastapi_users import models


class User(models.BaseUser):
    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
