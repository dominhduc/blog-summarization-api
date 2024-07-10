FROM python:3.8-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install flask transformers torch

# Copy application code
COPY . /app
WORKDIR /app

# Run the application
CMD ["python", "app.py"]
