# Use Python image as base image
FROM python:3-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3-tk gdal-bin proj-bin libproj-dev libspatialindex-dev libgdal-dev gcc g++ xvfb xauth

# Upgrade pip
RUN pip install --upgrade pip

# Install OSMnx dependencies
RUN pip install geopandas shapely

# Install OSMnx and matplotlib with verbose output
RUN pip install -vvv osmnx matplotlib

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY bird-view-gui.py /app/

# Set up Xvfb
ENV DISPLAY=:99

# Command to run the script
CMD xvfb-run -a python bird-view-gui.py
