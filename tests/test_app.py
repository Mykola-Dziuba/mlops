from fastapi.testclient import TestClient
from app.api import app  # import the FastAPI app

client = TestClient(app)  # use 'app', not 'api'


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
