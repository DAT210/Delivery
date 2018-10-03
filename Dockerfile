FROM python:3.7

LABEL Author="Group 2"

WORKDIR /app

COPY src /app

RUN pip install --trusted-host pypi.python.org -r docker_files/requirements.txt

EXPOSE 80

ENV NAME Delivery

CMD [ "python", "app.py" ]
