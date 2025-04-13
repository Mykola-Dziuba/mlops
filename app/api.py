# app/api.py
from fastapi import FastAPI
from app.models.iris import PredictRequest, PredictResponse
from ml.inference import load_model, predict

app = FastAPI()
model = load_model()  # Load once at startup


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_route(request: PredictRequest):
    result = predict(model, request.dict())
    return PredictResponse(prediction=result)
