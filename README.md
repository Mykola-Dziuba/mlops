# Laboratory 1 – MLOps-FastAPI Application

## Overview

This repository contains the solution for **Laboratory 1 – MLOps Application**.  
The goal is to implement a production-level ML system using FastAPI, `uv`, and MLOps best practices.  
Work is organized into well-defined steps as per the assignment.

---

## Features

- Dependency management with `uv`
- Version control using Git and GitHub
- Pre-commit hooks (Ruff, Xenon)
- Environment and secret management
- Testing with Pytest
- FastAPI server with ML model endpoint
- Containerization with Docker & Docker Compose

## Run Locally

```bash
uv venv --python 3.12
uv init
uv add fastapi uvicorn scikit-learn
uv run uvicorn app:app --reload
```

## Completed Tasks

### 1. Dependency Management Setup (2 points)

- Project initialized with `uv`, using `pyproject.toml` and `uv.lock`
- Production dependencies added:
  - `torch`, `transformers`, `joblib`, `clean-text`, `cloudpickle`
- Development dependencies added:
  - `mypy`, `pytest`
- Groups separated using `--dev` flag in `uv`
- PyTorch set up for available platform (CPU/GPU)

### Example commands used:

```bash
uv init
uv add clean-text joblib torch transformers cloudpickle
uv add --dev ruff mypy pytest
```

### 2. Pre-commit hooks (1 point)

Pre-commit hooks have been configured in .pre-commit-config.yaml and are triggered automatically on each commit.
The following tools are used:

ruff – linter
ruff-format – auto-formatter
mypy – static type checker

Example output during commit:

```
$ git commit -m "style: fix ruff-format formatting in **init**.py"
ruff.....................................................................Passed
ruff-format..............................................................Passed
Xenon....................................................................Passed
[main 2419b8d] style: fix ruff-format formatting in **init**.py
2 files changed, 3 insertions(+)
All hooks passed successfully
```

### 3. Webserver development (2 points)

FastAPI webserver implemented with a working /predict POST endpoint.
Input and output are validated using Pydantic models (PredictRequest, PredictResponse).
The model returns correct predictions.

```
curl -X POST \mlops$ curl -X POST \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "What a great MLOps lecture, I am very satisfied"}'
{"detail":[{"type":"missing","loc":["body","sepal_length"],"msg":"Field required","input":{"text":"What a great MLOps lecture, I am very satisfied"}},{"type":"missing","loc":["body","sepal_width"],"msg":"Field required","input":{"text":"What a great MLOps lecture, I am very satisfied"}},{"type":"missing","loc":["body","petal_length"],"msg":"Field required","input":{"text":"What a great MLOps lecture, I am very satisfied"}},{"type":"missing","loc":["body","petal_width"],"msg":"Field required","input":{"text":"What a great MLOps lecture, I am very satisfied"}}]}
```

### 3. Sentiment analysis implementation (2 points)

The sentiment analysis model was successfully loaded from inference_class.pkl using cloudpickle. The .predict() method is used for inference. A /predict POST endpoint is available via FastAPI for sentiment prediction.

```
curl -X POST http://localhost:8000/predict \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"text": "This MLOps lab was extremely helpful!"}'
```

```
{ "prediction": "positive" }
```

### 4. Code testing (1 point)

All unit tests have been successfully implemented and passed using pytest.

Coverage includes:
Root and health endpoints (test_app.py)
App settings validation (test_settings.py)
Sentiment analysis model:
Valid and invalid input handling
Model inference
JSON response structure (test_sentiment.py)

```
tests/test_app.py ..
tests/test_sentiment.py ...
tests/test_settings.py .
6 passed in 2.58s
```

### 5. Containerization (2 points):

The FastAPI-based sentiment analysis service is fully containerized using Docker and Docker Compose. It includes all code, dependencies, and the trained model.

To build and run the app:

```
git clone <repo_url>
cd mlops  # or the cloned repo folder
docker compose build --no-cache
docker compose up
```

Once running, the service will be available at:

http://localhost:8000

You can test it using Swagger UI or curl:

```
curl -X POST http://localhost:8000/predict \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"text": "This lab was very helpful!"}'
```

Expected response:

```
{ "prediction": "positive" }
```
