from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

user_board_association = Table(
    'user_board_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('board_id', Integer, ForeignKey('boards.id'))
)
