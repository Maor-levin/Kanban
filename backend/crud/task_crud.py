# crud/task_crud.py

from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.task_model import TaskModel
from models.board_model import BoardModel
from models.user_model import UserModel
from schemas.task_schemas import TaskCreate, TaskUpdate

def create_task(db: Session, task_data: TaskCreate, current_user: UserModel):
    """
    Creates a new task under the specified board if the board belongs to the current user.
    """
    board = (
        db.query(BoardModel)
        .filter(
            BoardModel.id == task_data.board_id,
            BoardModel.owner_id == current_user.id
        )
        .first()
    )

    if not board:
        raise HTTPException(
            status_code=404,
            detail="Board not found or you do not have permission."
        )

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
    """
    Retrieves all tasks for a given board, ensuring the board belongs to the current user.
    """
    tasks = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(
            BoardModel.id == board_id,
            BoardModel.owner_id == current_user.id
        )
        .all()
    )
    return tasks


def update_task_status(db: Session, task_id: int, task_update: TaskUpdate, current_user: UserModel):
    """
    Updates the task's fields (title, status, etc.) if the task belongs to the current user.
    """
    task = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(
            TaskModel.id == task_id,
            BoardModel.owner_id == current_user.id
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found or you do not have permission."
        )

    # Update fields if they are provided (assuming TaskUpdate allows optional fields)
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.status is not None:
        task.status = task_update.status

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int, current_user: UserModel):
    """
    Deletes a task if it belongs to the current user.
    """
    task = (
        db.query(TaskModel)
        .join(BoardModel)
        .filter(
            TaskModel.id == task_id,
            BoardModel.owner_id == current_user.id
        )
        .first()
    )
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found or you do not have permission."
        )

    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}
