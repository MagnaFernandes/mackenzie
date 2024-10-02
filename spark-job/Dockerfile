FROM spark:3.3.0-hadoop3.2 
WORKDIR /app
COPY spark_job.py .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymongo
CMD ["spark-submit", "--master", "local[*]", "spark_job.py"]