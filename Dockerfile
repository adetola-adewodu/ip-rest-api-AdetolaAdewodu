# Use a Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the Flask app will run on
EXPOSE 5000

# Set an environment variable for Flask
ENV FLASK_APP=app.py 

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]