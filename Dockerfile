# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install system dependencies (e.g., ffmpeg)
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

# Copy your Python script into the container
COPY synthesize_speech.py .

# Specify the default command to run when the container starts
CMD ["python", "/app/synthesize_speech.py"]

