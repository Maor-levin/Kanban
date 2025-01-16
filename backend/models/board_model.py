# backend/models/board_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from models.association_model import user_board_association



class BoardModel(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tasks = relationship("TaskModel", back_populates="board")
    
    users = relationship(
        'User',
        secondary=user_board_association,
        back_populates='boards'
    )
    invitations = relationship('Invitation', back_populates='board')
