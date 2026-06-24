# Create a Dockerized Python application that uses the python:3.12-slim image as the base image. 
# Develop a Python script that prints the current Python version running inside the container along with the current date and time.
#Create a Dockerfile that copies the Python script into the container and executes it automatically when the container starts.
#The application should successfully build and run using Docker commands. Push the complete project, including the Python script, Dockerfile, requirements file (if required), and README documentation, to a GitHub repository.
#The README should contain instructions for building and running the Docker image and should include a sample output screenshot.
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt
COPY app.py .
CMD ["python", "app.py"]