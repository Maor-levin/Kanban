from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    status: str = "To Do" 

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    board_id: int 
    class Config:
        orm_mode = True
