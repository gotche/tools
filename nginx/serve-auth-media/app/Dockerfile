FROM python:3.6.1-alpine
MAINTAINER yo "yo yo"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP wsgi.py
CMD ["flask", "run", "--host=0.0.0.0"]
