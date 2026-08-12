from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .master("local[*]") \
    .getOrCreate()

# Test with a simple operation
df = spark.createDataFrame(
    [("Hello", 1), ("World", 2)],
    ["word", "count"])

df.show()

# Stop the session
spark.stop()