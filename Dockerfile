# Creating Dockerfile

# Create a image of python with linux distribuition.
FROM python:3.9.6-alpine3.13
# Set directory
WORKDIR /Moscow_Ring_Road_Coordinates
# Copy contents of directory.
ADD . /Moscow_Ring_Road_Coordinates
# Install Packages of project.
RUN pip install --no-cache -r requirements.txt
# Run command line to start container.
CMD [ "python", "./myapp/app.py" ]

# Commands
# Create and build image: docker image build -t moscow_ring_road_coordinates .
# List images: docker image ls 