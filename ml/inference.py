# ml/inference.py
from joblib import load
import numpy as np


def load_model(path="ml/model.joblib"):
    # Load model from file
    return load(path)


def predict(model, features: dict) -> str:
    # Convert dict to numpy array and predict
    input_array = np.array(
        [
            [
                features["sepal_length"],
                features["sepal_width"],
                features["petal_length"],
                features["petal_width"],
            ]
        ]
    )
    prediction = model.predict(input_array)
    return str(prediction[0])
