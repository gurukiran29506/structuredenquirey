# Use official Python slim image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . .

# Default command to run your Python app
CMD ["python", "car.py"]
