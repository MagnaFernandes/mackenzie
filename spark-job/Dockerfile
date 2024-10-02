FROM spark:3.3.0-hadoop3.2  # Or another suitable Spark image

WORKDIR /app
COPY spark_job.py .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# You might need to install PyMongo inside the docker image
RUN pip install pymongo

CMD ["spark-submit", "--master", "local[*]", "spark_job.py"]