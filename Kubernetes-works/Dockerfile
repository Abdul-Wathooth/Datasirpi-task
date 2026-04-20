# Use the official Python 3.11 image as the base image
FROM python:3.11                

# Set the working directory inside the container to /web

WORKDIR /web

# Copy everything from your current local directory to the container's /web directory
COPY  . .

# Copy the requirements file (need.txt) into the container
COPY need.txt .

# Install all Python dependencies listed in need.txt
RUN pip install -r need.txt

# Inform Docker that the container will listen on port 5000
EXPOSE 5000

# This runs your Flask app
CMD ["python","app.py"]
