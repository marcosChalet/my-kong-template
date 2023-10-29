FROM python:3.8

WORKDIR /app

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY conf.json /app/conf.json
COPY plugins.json /app/plugins.json

RUN pip install -r /app/requirements.txt


CMD [ "python", "app.py" ]