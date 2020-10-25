FROM python:3.8-alpine

# EXPOSE instruction indicates the ports on which a container
# will listen for connections
# apps listen to port 5000
EXPOSE 5000


# Set working directory for COPY and CMD instructions
WORKDIR /flask_app/app


COPY . /flask_app/app


RUN pip install -r requirements.txt


ENTRYPOINT ["python"]

CMD ["app.py"]