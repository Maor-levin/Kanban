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


# Define allowed origins
origins = [
    "http://localhost:3000",  # Frontend URL

]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allowed origins
    allow_credentials=True,           # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],              # Allow all HTTP methods
    allow_headers=["*"],              # Allow all headers
)

# Include your routers
app.include_router(user_router, prefix="/users")
app.include_router(task_router, prefix="/api")
app.include_router(board_router, prefix="/api")
