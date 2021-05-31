from fastapi_users import FastAPIUsers
from user.logic import user_db, auth_backends, SECRET
from user.schemas import User, UserCreate, UserUpdate, UserDB

fastapi_users = FastAPIUsers(
    # об'єкт користувач
    user_db,

    # список наших методів авторизації, в нашому випадку JWT auth
    auth_backends,

    # схеми таблиць user
    User,
    UserCreate,
    UserUpdate,
    UserDB,

    # secret key
    SECRET,
)
