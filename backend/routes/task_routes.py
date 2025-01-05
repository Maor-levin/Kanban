from fastapi import APIRouter, Depends, HTTPException, status  
from sqlalchemy.orm import Session

from db.connection import SessionLocal
from models.task_model import TaskModel
from models.board_model import BoardModel
from models.user_model import UserModel
from schemas.task_schemas import TaskCreate, TaskOut, TaskUpdate
from auth.dependencies import get_current_user, get_db

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Check if the board belongs to the current user
    board = db.query(BoardModel).filter(
        BoardModel.id == task_data.board_id,
        BoardModel.owner_id == current_user.id
    ).first()

    if not board:
        raise HTTPException(status_code=404, detail="Board not found or not yours")

    # Create a new task associated with the board
    new_task = TaskModel(
        title=task_data.title,
        status=task_data.status,
        board_id=board.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks", response_model=list[TaskOut])
def get_tasks(
    board_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Return tasks only for the given board (owned by user)
    tasks = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(BoardModel.id == board_id, BoardModel.owner_id == current_user.id)
        .all()
    )
    return tasks

@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task_status(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Fetch the task ensuring it belongs to the current user
    task = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(TaskModel.id == task_id, BoardModel.owner_id == current_user.id)
        .first()
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not yours")

    # Update the task's status
    task.status = task_update.status
    db.commit()
    db.refresh(task)
    return task

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):

    # Fetch the task ensuring it belongs to the current user
    task = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(TaskModel.id == task_id, BoardModel.owner_id == current_user.id)
        .first()
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found or not yours")

    # Delete the task
    db.delete(task)
    db.commit()

    # No content to return
    return