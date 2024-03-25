from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    task:str

    class Config():
        orm_model = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    todos:List[Todo] = []

    class Config():
        orm_model = True

class ShowTodo(BaseModel):
    task:str
    creator:ShowUser

    class Config():
        orm_model = True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None