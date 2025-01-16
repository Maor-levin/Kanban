from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas.user_schemas import UserCreate, UserOut, UserLogin
from auth.auth_utils import create_access_token
from crud.user_crud import get_user_by_username, create_user, verify_password

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    new_user = create_user(db, user_data)
    return UserOut(id=new_user.id, username=new_user.username)

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_data.username)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
