# —— Great Expectations setup ——  
import great_expectations as ge
from great_expectations.checkpoint import SimpleCheckpoint

# Tell GE where your expectation and checkpoint YAML live:
data_context_root_dir = "/Workspace/Repos/your‑user/azure‑data‑quality‑framework/dq"

# Create a DataContext object:
context = ge.data_context.DataContext(data_context_root_dir)
# Databricks notebook source
# 01_ingest_streaming.py
# Sample PySpark notebook to ingest from Azure Event Hub into a Delta Lake bronze table

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType

# ——————————————  
# 1. Initialize Spark  
spark = SparkSession.builder \
    .appName("EH_Stream_Ingest") \
    .getOrCreate()

# ——————————————  
# 2. Set your Event Hub connection string  
# Replace <...> with your real values or mount them via Databricks secrets
connectionString = "Endpoint=sb://<your-namespace>.servicebus.windows.net/;SharedAccessKeyName=<key-name>;SharedAccessKey=<key>;EntityPath=<hub-name>"
ehConf = {
  "eventhubs.connectionString": connectionString
}

# ——————————————  
# 3. Read streaming data  
streamDF = spark.readStream \
    .format("eventhubs") \
    .options(**ehConf) \
    .load()

# The body arrives as binary; cast to string  
messages = streamDF.selectExpr(
    "CAST(body AS STRING) as message",
    "enqueuedTime as event_time"
)

# ——————————————  
# 4. Write to Delta Lake (bronze)  
checkpoint_path = "/mnt/delta/bronze/_checkpoints/stream_ingest"
output_path     = "/mnt/delta/bronze/stream_ingest"

query = messages.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", checkpoint_path) \
    .start(output_path)

# Let the stream run until manually stopped in Databricks UI  
# query.awaitTermination()
