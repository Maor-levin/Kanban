from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.task_schemas import TaskCreate, TaskOut, TaskUpdate
from auth.dependencies import get_current_user, get_db
from crud.task_crud import create_task, get_tasks, update_task_status, delete_task

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_task_endpoint(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return create_task(db, task_data, current_user)

@router.get("/tasks", response_model=list[TaskOut])
def get_tasks_endpoint(
    board_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return get_tasks(db, board_id, current_user)

@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task_status_endpoint(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return update_task_status(db, task_id, task_update, current_user)

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    delete_task(db, task_id, current_user)
    return
