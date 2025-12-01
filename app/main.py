"""
FastAPI application exposing a small tasks API.

Endpoints:
- GET /health         -> health check
- GET /tasks          -> list tasks
- POST /tasks         -> create a new task
- PATCH /tasks/{id}   -> update a task
- DELETE /tasks/{id}  -> delete a task

Author: Harsh Kumar
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, status

from .database import task_repository
from .models import Task, TaskCreate, TaskUpdate

app = FastAPI(
    title="Mini Backend Service",
    version="0.1.0",
    description="A small FastAPI backend by Harsh Kumar.",
)


@app.get("/health")
def health_check() -> dict:
    """Simple health endpoint useful for monitoring."""
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    """Return all tasks."""
    return task_repository.list_tasks()


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    """Create a new task."""
    return task_repository.create_task(payload)


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    """Update a task partially."""
    task = task_repository.update_task(task_id, payload)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    """Delete a task."""
    deleted = task_repository.delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
