# ml/training.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from joblib import dump


def load_data():
    # Load iris dataset
    data = load_iris()
    return data.data, data.target


def train_model(X, y):
    # Train simple random forest
    model = RandomForestClassifier()
    model.fit(X, y)
    return model


def save_model(model, path="ml/model.joblib"):
    # Save model to file
    dump(model, path)
