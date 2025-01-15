from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.connection import engine
from models.base import Base

from routes.user_routes import router as user_router
from routes.task_routes import router as task_router
from routes.board_routes import router as board_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


origins = [
    "http://localhost:3000"  
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,         
    allow_methods=["*"],             
    allow_headers=["*"],              
)

# Include your routers
app.include_router(user_router, prefix="/users")
app.include_router(task_router, prefix="/api")
app.include_router(board_router, prefix="/api")
