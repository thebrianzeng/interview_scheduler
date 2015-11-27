# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER thebrianzeng <thebrianzeng@gmail.com>

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Copy the application folder inside the container
ADD . /interview_scheduler

# Get pip to download and install requirements:
RUN pip install -r /interview_scheduler/config/requirements.txt

# Expose ports
EXPOSE 5000 

# Set the default directory where CMD will execute
WORKDIR /interview_scheduler

# Default command to execute
CMD gunicorn --bind 0.0.0.0:5000 app:app
