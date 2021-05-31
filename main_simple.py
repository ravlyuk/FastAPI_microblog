import uvicorn
from fastapi import FastAPI

app = FastAPI()

# ================== Простий приклад


# @app.get("/user")
# async def root():
#     return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

# ================== Аргументи


# @app.get("/user/{username}")
# async def root(username: str):
#     return {"message": username}

# ================== Клас схема

# from pydantic import BaseModel
#
#
# # це наша клас-схема, наш сериалізатор і десериалізтор
# class User(BaseModel):
#     id: int
#     username: str
#     password: str
#     email: str
#
#
# @app.post("/user/")
# async def root(user: User):
#     return {"message": user}


# ================== Клас схема може не тілкьи приймати дані а і віддавати

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str
    email: str


@app.get("/user/", response_model=User)
async def root():
    user = {
        "id": "2",
        "username": "Anna",
        "password": "password2021",
        "email": "anna@gmail.com"

    }
    return user
