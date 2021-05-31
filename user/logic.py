from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from core.db import database
from .models import users
from .schemas import UserDB

user_db = SQLAlchemyUserDatabase(
    UserDB,  # схема
    database,  # база
    users  # модель
)

SECRET = "7kjkhjkk69yiey3jhlljgk768kjhkhjhkhjkfgdfgdfgdfjlj676469kjh"

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=120 * 60),
]
