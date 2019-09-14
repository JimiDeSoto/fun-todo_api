FROM python:3.8.0b4-alpine3.10 
RUN apk update && apk upgrade
RUN pip install flask
RUN pip install flask-httpauth

COPY app.py /opt/app.py

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0

