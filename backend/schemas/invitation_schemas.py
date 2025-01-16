from pydantic import BaseModel
from enum import Enum

class InvitationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    declined = "declined"

class InvitationCreate(BaseModel):
    board_id: int
    recipient_username: str

class InvitationResponse(BaseModel):
    id: int
    board_id: int
    sender_id: int
    recipient_id: int
    status: InvitationStatus

    class Config:
        orm_mode = True
