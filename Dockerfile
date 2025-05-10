# Stage 1: Build dependencies
# Use a smaller, lightweight base image (python:3.12-alpine) for reduced image size
FROM python:3.12-alpine as builder

# Set working directory to /app
WORKDIR /app

# Install system dependencies, such as compilers and libraries for building
RUN apk add --no-cache \
    curl \
    make \
    gcc \
    g++ \
    libc6-compat \
    libffi-dev \
    && pip install --upgrade pip setuptools

# Install and configure 'uv' (Uvicorn), used to run the FastAPI app
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    ln -s /root/.local/bin/uv /usr/local/bin/uv

# Copy only the dependency files (pyproject.toml, uv.lock) to install dependencies
COPY pyproject.toml uv.lock ./ 

# Install dependencies using 'uv sync'
RUN uv sync

# Stage 2: Runtime image (copy only necessary files)
# Use the same lightweight base image for runtime
FROM python:3.12-alpine as runtime

# Set the working directory to /app
WORKDIR /app

# Copy over the installed dependencies from the builder stage
COPY --from=builder /root/.local /root/.local

# Copy the application code from the build context
COPY . .

# Install torch manually using the official wheel (for Alpine)
RUN pip install torch==2.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Expose port 8000 for the FastAPI application to be accessible
EXPOSE 8000

# Set the default command to run the FastAPI app with Uvicorn
CMD ["uv", "run", "uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
