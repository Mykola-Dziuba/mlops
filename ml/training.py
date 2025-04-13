# ml/training.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    # Load the Iris dataset
    data = load_iris()
    return data.data, data.target


def train_model(X, y):
    # Train a simple classifier
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, path: str = "ml/model.joblib"):
    # Save model to disk
    joblib.dump(model, path)
