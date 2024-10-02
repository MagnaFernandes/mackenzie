FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY spark_job.py .
CMD ["spark-submit", "--master", "local[*]", "spark_job.py"]