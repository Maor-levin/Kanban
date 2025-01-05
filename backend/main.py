from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker, scoped_session
from db.connection import engine
from models.base import Base


from models.base import Base
from models.user_model import UserModel
from models.task_model import TaskModel
from models.board_model import BoardModel
from routes.user_routes import router as user_router
from routes.task_routes import router as task_router
from routes.board_routes import router as board_router

# Create all tables (simple approach)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include your routers
app.include_router(user_router, prefix="/users")
app.include_router(task_router, prefix="/api")
app.include_router(board_router, prefix="/api")
