# backend/routes/user_routes.py
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from db.connection import SessionLocal
from models.user_model import UserModel
from schemas.user_schemas import UserCreate, UserOut, UserLogin
from auth.auth_utils import create_access_token

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(UserModel.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = pwd_context.hash(user_data.password)
    new_user = UserModel(username=user_data.username, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserOut(id=new_user.id, username=new_user.username)

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.username == user_data.username).first()
    if not user or not pwd_context.verify(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
