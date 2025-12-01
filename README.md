<<<<<<< HEAD
# Mini Backend – FastAPI Tasks API

Author: Harsh Kumar

A minimal yet production-style backend implemented in FastAPI.

It exposes a small set of RESTful endpoints for managing "tasks" and
includes unit tests using FastAPI's TestClient.

---

## Endpoints

- `GET /health` – Health check
- `GET /tasks` – List all tasks
- `POST /tasks` – Create a new task
- `PATCH /tasks/{id}` – Update a task
- `DELETE /tasks/{id}` – Delete a task

---

## Tech Stack

- FastAPI
- Pydantic
- Uvicorn
- Pytest

---

## Setup

```bash
git clone https://github.com/<your-username>/mini-backend.git
cd mini-backend

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
=======
# mini-backend-fastapi
A minimal, production-grade FastAPI backend with CRUD tasks and tests. Tech: FastAPI, Pydantic, Uvicorn, Pytest.
>>>>>>> 0e1dca1020481ea6d0b25c07a52cfe40c05b9a34
