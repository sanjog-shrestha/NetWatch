FROM python:3.11-slim

WORKDIR /app

#Install system dependencies for ping (optional, ping3 users raw sockets)
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY src/ ./src/

# Create log directory
RUN mkdir -p logs 

CMD [ "python", "src/monitor.py" ]