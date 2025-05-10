# tests/test_sentiment.py

from fastapi.testclient import TestClient
from app.api import app
import cloudpickle
import os

client = TestClient(app)


def test_sentiment_model_loads():
    path = "app/artifacts/inference_class.pkl"
    assert os.path.exists(path)
    with open(path, "rb") as f:
        model_class = cloudpickle.load(f)
    assert callable(getattr(model_class, "predict", None))


def test_sentiment_valid_input():
    response = client.post("/predict", json={"text": "This course is amazing!"})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], str)


def test_sentiment_invalid_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422
