# ml/inference.py
import joblib
from sklearn.datasets import load_iris


def load_model(path: str = "ml/model.joblib"):
    # Load model from file
    return joblib.load(path)


def predict(model, features: dict) -> str:
    # Predict the class index
    prediction_index = model.predict([list(features.values())])[0]

    # Map index to class name
    class_names = load_iris().target_names
    return class_names[prediction_index]
