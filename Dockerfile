# Stage 1: Build environment
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (same as Flask app)
EXPOSE 5000

# Command to run the app
CMD ["python3", "app.py"]

