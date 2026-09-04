FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source and static files
COPY app/ ./app/
COPY static/ ./static/

# Environment defaults
ENV PORT=8000
EXPOSE 8000

# Start FastAPI application using dynamic port for Cloud platforms (Render, Railway, etc.)
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
