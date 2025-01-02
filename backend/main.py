from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Kanban API"}


@app.get("/tasks")
def get_tasks():
    # Placeholder for task retrieval logic
    return {"tasks": []}
