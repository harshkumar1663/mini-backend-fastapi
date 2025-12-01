from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_task():
    # Create
    payload = {"title": "Test Task", "description": "Sample", "completed": False}
    create_res = client.post("/tasks", json=payload)
    assert create_res.status_code == 201
    data = create_res.json()
    assert data["title"] == "Test Task"

    # List
    list_res = client.get("/tasks")
    assert list_res.status_code == 200
    tasks = list_res.json()
    assert any(t["title"] == "Test Task" for t in tasks)
