# Stage 1: Build stage
FROM python:3.9-slim as builder

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy only the files necessary for installing dependencies
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# --no-root: don't install the project itself
# --no-dev: don't install dev dependencies
RUN poetry install --no-root --no-dev

# Stage 2: Final application stage
FROM python:3.9-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv /.venv

# Activate the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy the application source code
COPY src/ ./src

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# The host must be 0.0.0.0 to be accessible from outside the container
CMD ["uvicorn", "src.ascv_genai.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
