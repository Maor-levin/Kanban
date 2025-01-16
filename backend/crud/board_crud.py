from sqlalchemy.orm import Session
from models.board_model import BoardModel
from models.user_model import UserModel
from schemas.board_schemas import BoardCreate
from fastapi import HTTPException


def create_board(db: Session, board: BoardCreate, current_user: UserModel):
    new_board = BoardModel(name=board.name, owner_id=current_user.id)
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board

def list_boards(db: Session, current_user: UserModel):
    boards = db.query(BoardModel).filter(BoardModel.owner_id == current_user.id).all()
    return boards

def share_board(db: Session, board_id: int, target_username: str, current_user: UserModel):
    board = db.query(BoardModel).filter(
        BoardModel.id == board_id,
        BoardModel.owner_id == current_user.id
    ).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board not found or not owned by you")

    target_user = db.query(UserModel).filter(UserModel.username == target_username).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Target user not found")

    board.users.append(target_user)
    db.commit()
    return {"message": "Board shared successfully"}


def accept_shared_board(db: Session, board_id: int, current_user: UserModel):
    board = db.query(BoardModel).filter(BoardModel.id == board_id).first()
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")

    if current_user not in board.users:
        board.users.append(current_user)
        db.commit()
    return {"message": "Board accepted successfully"}

def list_boards(db: Session, current_user: UserModel):
    owned_boards = db.query(BoardModel).filter(BoardModel.owner_id == current_user.id).all()
    shared_boards = db.query(BoardModel).join(BoardModel.users).filter(UserModel.id == current_user.id).all()
    return owned_boards + shared_boards
