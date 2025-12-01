"""
In-memory "database" for tasks.

For a small demo backend, we use a Python list. The abstraction is still
split out so that you can later plug in a real database (PostgreSQL, etc).

Author: Harsh Kumar
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from .models import Task, TaskCreate, TaskUpdate


class TaskRepository:
    """
    Simple repository handling CRUD for tasks in memory.
    """

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def list_tasks(self) -> List[Task]:
        return list(self._tasks.values())

    def create_task(self, data: TaskCreate) -> Task:
        task = Task(
            id=self._next_id,
            title=data.title,
            description=data.description,
            completed=data.completed,
            created_at=datetime.utcnow(),
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, data: TaskUpdate) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if not task:
            return None

        update_data = data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        self._tasks[task_id] = task
        return task

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False


# Singleton repository instance for app-wide usage
task_repository = TaskRepository()
