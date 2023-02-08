# Start from the official Python image
FROM python:3.10.7-slim-buster

# Set the working directory to /youtubot
WORKDIR /youtubot

# Copy the requirements.txt file to the container
COPY ./requirements.txt /youtubot/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy all the files from the local youtubot repo to the container
COPY . /youtubot


#RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"