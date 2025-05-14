# Use official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into the container
COPY . .

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
