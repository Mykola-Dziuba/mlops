# app/api.py
from fastapi import FastAPI
from app.models.text import PredictRequest, PredictResponse
from ml.sentiment_inference import load_inference, predict_sentiment

app = FastAPI()

# Load the sentiment analysis model once at startup
sentiment_model = load_inference()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_route(request: PredictRequest):
    # Run sentiment prediction
    result = predict_sentiment(sentiment_model, request.text)
    return PredictResponse(prediction=result)
