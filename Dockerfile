# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=8888

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
