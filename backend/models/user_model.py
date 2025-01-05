# backend/models/user_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
