FROM python:3.7-slim

LABEL Author="Group 2"

WORKDIR /app

COPY docker_files/requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app

EXPOSE 80

ENV NAME Delivery

CMD [ "python", "docker_files/app.py" ]
