FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "microservice.py", "run", "--port", "5000", "--host=0.0.0.0"]
EXPOSE 5000/tcp