from pydantic import BaseModel

class BoardBase(BaseModel):
    name: str

class BoardCreate(BoardBase):
    pass

class BoardOut(BoardBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
