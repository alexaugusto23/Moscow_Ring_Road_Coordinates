# Creating Dockerfile

# Create a image of python with linux distribuition.
FROM python:3.9.6-alpine3.13
# Copy contents of directory.
COPY . /Moscow_Ring_Road_Coordinates
# CD or LS directory.
WORKDIR /Moscow_Ring_Road_Coordinates
# Install Packages of project.
RUN pip install --no-cache -r requirements.txt
# CD or LS directory.
WORKDIR /Moscow_Ring_Road_Coordinates/myapp
# Run command line to start container.
CMD python app.py


# Commands
# Create and build image: docker image build -t moscow_ring_road_coordinates .
# Create and build image: docker build -t moscow_ring_road_coordinates .
# List images: docker image ls 
# Run image: docker run -p 5000:5000 -d moscow_ring_road_coordinates
# Stop: docker stop <id>