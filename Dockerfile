FROM python:3.12-slim

WORKDIR /app

# Install system dependencies needed for dynamic/static tools if required
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements template first for caching layers
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Entrypoint for the automated security pipeline
CMD ["python", "src/main.py"]
