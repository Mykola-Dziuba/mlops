# debug_model.py
import sys

sys.path.append("app")

import cloudpickle

with open("app/artifacts/inference_class.pkl", "rb") as file:
    Inference = cloudpickle.load(file)

print(Inference.__init__.__code__.co_varnames)
