
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Task
from services import (
    get_all_tasks,
    add_task as service_add_task,
    update_task as service_update_task,
    delete_task as service_delete_task,
    get_task_by_id,
    update_task_status as service_update_task_status,
)
from pydantic import BaseModel

class CreateTaskRequest(BaseModel):
    title: str
    description: str

class UpdateTaskRequest(BaseModel):
    title: str | None = None
    description: str | None = None

app = FastAPI(
    title="CLI Todo",
    description="A simple todo application that can be used from the CLI or via an API.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tasks", response_model=list[Task])
async def list_tasks():
    """
    Get all tasks.
    """
    return get_all_tasks()

@app.post("/tasks", response_model=Task)
async def create_task(task_request: CreateTaskRequest):
    """
    Create a new task.
    """
    return service_add_task(task_request.title, task_request.description)

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """
    Get a single task by ID.
    """
    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_request: UpdateTaskRequest):
    """
    Update a task.
    """
    return service_update_task(task_id, task_request.title, task_request.description)

@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    """
    Delete a task.
    """
    service_delete_task(task_id)
    return

@app.put("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int):
    """
    Mark a task as complete.
    """
    return service_update_task_status(task_id, "complete")

@app.put("/tasks/{task_id}/incomplete", response_model=Task)
async def incomplete_task(task_id: int):
    """
p    Mark a task as incomplete.
    """
    return service_update_task_status(task_id, "incomplete")
