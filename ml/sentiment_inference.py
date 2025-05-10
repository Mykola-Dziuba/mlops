# ml/sentiment_inference.py
import sys
import cloudpickle

# Ensure module resolution during deserialization
sys.path.append("app")


def load_inference(
    class_path="app/artifacts/inference_class.pkl", model_dir="app/artifacts"
):
    with open(class_path, "rb") as file:
        Inference = cloudpickle.load(file)
    return Inference(model_dir)


def predict_sentiment(model, text: str) -> str:
    return model.predict(text)
