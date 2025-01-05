from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connection import SessionLocal
from models.board_model import BoardModel
from models.user_model import UserModel
from schemas.board_schemas import BoardCreate, BoardOut
from auth.dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/boards", response_model=BoardOut)
def create_board(board: BoardCreate, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    new_board = BoardModel(name=board.name, owner_id=current_user.id)
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

@router.get("/boards", response_model=list[BoardOut])
def list_boards(current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    boards = db.query(BoardModel).filter(BoardModel.owner_id == current_user.id).all()
    return boards
