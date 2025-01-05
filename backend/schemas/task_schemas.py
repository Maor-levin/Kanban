from pydantic import BaseModel, Field, validator
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    status: str = Field("To Do", pattern="^(To Do|In Progress|Done)$") 

    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["To Do", "In Progress", "Done"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v

class TaskCreate(TaskBase):
    board_id: int = Field(..., description="ID of the board to which the task belongs")

class TaskUpdate(BaseModel):
    status: str = Field(..., description="New status of the task")

    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ["To Do", "In Progress", "Done"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v

class TaskOut(TaskBase):
    id: int
    board_id: int 

    class Config:
        orm_mode = True
