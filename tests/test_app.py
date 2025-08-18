import json
from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data["status"] == "UP"

def test_create_task():
    client = app.test_client()
    res = client.post("/tasks", json={"title": "New Task"})
    assert res.status_code == 201
    data = json.loads(res.data)
    assert data["title"] == "New Task"
    assert data["done"] is False

