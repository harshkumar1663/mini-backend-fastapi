"""
Pydantic models for the mini backend.

We model a simple "Task" entity to demonstrate CRUD-style endpoints.

Author: Harsh Kumar
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Incoming payload when creating a task."""
    title: str = Field(..., min_length=3, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = False


class TaskUpdate(BaseModel):
    """Incoming payload when updating a task."""
    title: Optional[str] = Field(default=None, min_length=3, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None


class Task(TaskCreate):
    """Full task representation with server-generated fields."""
    id: int
    created_at: datetime
