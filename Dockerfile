# Dockerfile

# 1. Use minimal base image with Python 3.12
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Install uv and link to PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    ln -s /root/.local/bin/uv /usr/local/bin/uv

# 5. Copy only dependency files
COPY pyproject.toml uv.lock ./

# 6. Sync dependencies from lockfile
ENV UV_HTTP_TIMEOUT=120
RUN uv sync

# 7. Copy application code
COPY . .

# 8. Expose port for FastAPI
EXPOSE 8000

# 9. Run FastAPI app
CMD ["uv", "run", "uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
