# Start with a base image containing Python runtime
FROM python:3.8-slim

# Set the working directory in the Docker container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
        perl \
        gcc \
        python3-dev \
        vim \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add the requirements.txt to Docker container and install packages
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Start JupyterLab
CMD ["jupyter", "lab", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]

