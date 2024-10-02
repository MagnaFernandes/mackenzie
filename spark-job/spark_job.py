from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
import pymongo

spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

# Read data from MongoDB
client = pymongo.MongoClient("mongodb://mongodb:27017")
db = client["your_database_name"]

cdc_df = spark.read.format("com.mongodb.spark.sql.DefaultSource")\
    .option("uri", f"mongodb://mongodb:27017/your_database_name.asd_data_cdc")\
    .load()

faker_df = spark.read.format("com.mongodb.spark.sql.DefaultSource")\
    .option("uri", f"mongodb://mongodb:27017/your_database_name.asd_data_faker")\
    .load()

# Perform transformations (example)
transformed_df = cdc_df.join(faker_df, cdc_df.id == faker_df.id, "inner")\
    .withColumn("combined_data", lit("Combined CDC and Faker data"))


# Write to MongoDB
transformed_df.write.format("com.mongodb.spark.sql.DefaultSource")\
    .option("uri", f"mongodb://mongodb:27017/your_database_name.asd_data_inc")\
    .mode("append")\
    .save()

spark.stop()