from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.board_schemas import BoardCreate, BoardOut
from auth.dependencies import get_current_user, get_db
from crud.board_crud import create_board, list_boards, share_board, accept_shared_board

router = APIRouter()

@router.post("/boards", response_model=BoardOut)
def create_board_endpoint(
    board: BoardCreate,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return create_board(db, board, current_user)

@router.get("/boards", response_model=list[BoardOut])
def list_boards_endpoint(
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return list_boards(db, current_user)


@router.post("/boards/{board_id}/share")
def share_board_endpoint(
    board_id: int,
    target_username: str,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return share_board(db, board_id, target_username, current_user)

@router.post("/boards/{board_id}/accept")
def accept_shared_board_endpoint(
    board_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return accept_shared_board(db, board_id, current_user)

