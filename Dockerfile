FROM python:3.8-slim-buster

WORKDIR /app
RUN pip3 install requests

COPY . .

CMD [ "python3", "it-test.py"]