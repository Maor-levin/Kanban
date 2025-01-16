from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from .association_model import user_board_association  

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    boards = relationship(
        "BoardModel",
        secondary=user_board_association,
        back_populates="users"
    )
