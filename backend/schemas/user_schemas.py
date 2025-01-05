# backend/schemas/user_schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

class UserLogin(BaseModel):
    username: str
    password: str
