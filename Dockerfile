# MAaaS - Multi-Agent as a Service Enterprise Platform
# Production Dockerfile using Python 3.9 Slim

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies (Required for robust Python packages)
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p clients factory_logs archives ops reports memory

# Expose ports
# 8501: Streamlit frontend (The Investor Dashboard)
EXPOSE 8501

# --- CONFIGURATION SWITCH ---
# OPTION 1: Run Backend API (Commented out for Demo)
# CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000"]

# OPTION 2: Run MAaaS Dashboard (Active for Investor Demo)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]