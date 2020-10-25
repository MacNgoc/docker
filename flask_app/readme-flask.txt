# To build an image, use this:
docker build -t myimage:v2 -f Dockerfile . 

# TO run a container from an image
docker run -d -p 5000:5000 myimage:v1
