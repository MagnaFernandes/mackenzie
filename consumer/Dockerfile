FROM python:3.9-slim-buster

WORKDIR /app

COPY consumer.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "consumer.py"]