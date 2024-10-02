FROM spark:python3
WORKDIR /app
COPY spark_job.py .
COPY requirements.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt
CMD ["spark-submit", "--master", "local[*]", "spark_job.py"]