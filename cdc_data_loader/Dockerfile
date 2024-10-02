FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY cdc_loader.py .
CMD ["python", "cdc_loader.py"]