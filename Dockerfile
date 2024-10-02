# Use a Python base image
FROM python:3.9
LABEL authors="jeromeazah"
# Set work directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run the app
CMD ["python", "app.py"]
