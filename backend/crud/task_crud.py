from sqlalchemy.orm import Session
from models.task_model import TaskModel
from models.board_model import BoardModel
from models.user_model import UserModel
from schemas.task_schemas import TaskCreate, TaskUpdate
from fastapi import HTTPException


def create_task(db: Session, task_data: TaskCreate, current_user: UserModel):
    board = db.query(BoardModel).filter(
        BoardModel.id == task_data.board_id,
        BoardModel.owner_id == current_user.id
    ).first()

    if not board:
        raise HTTPException(status_code=404, detail="Board not found or not yours")

    new_task = TaskModel(
        title=task_data.title,
        status=task_data.status,
        board_id=board.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session, board_id: int, current_user: UserModel):
    tasks = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(BoardModel.id == board_id, BoardModel.owner_id == current_user.id)
        .all()
    )
    return tasks

def update_task_status(db: Session, task_id: int, task_update: TaskUpdate, current_user: UserModel):
    task = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(TaskModel.id == task_id, BoardModel.owner_id == current_user.id)
        .first()
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not yours")

    task.sta
