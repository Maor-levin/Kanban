from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user_model import UserModel
from schemas.user_schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def create_user(db: Session, user_data: UserCreate):
    hashed_password = pwd_context.hash(user_data.password)
    new_user = UserModel(username=user_data.username, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
