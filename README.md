# Laboratory 1 – MLOps-FastAPI Application

## Overview

This project demonstrates a complete MLOps pipeline by building a production-ready machine learning application using FastAPI and `uv`. It includes model training, environment configuration, code quality enforcement, and Docker-based deployment.

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
