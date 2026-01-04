FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port (Documentation only, Render ignores this but good practice)
EXPOSE 5000

# Use ENTRYPOINT to allow CLI args
CMD ["python", "app.py"]