# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install missing dependencies.
RUN apt-get update &&  \
    apt-get upgrade -y &&  \
    apt-get install -y \
    libsm6 libxext6 libxrender-dev \
    wget \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the app directory contents into the container at /app
COPY serve /app

# Copy the models directory into the container at /app/models
COPY models /app/models

# Expose port 8000
EXPOSE 8000

# Specify the command to run your application
CMD ["python", "main.py"]