from pyspark.sql import SparkSession

spark = SparkSession.builder \
   .appName("PySpark Test") \
   .master("local[*]") \
   .getOrCreate()

df = spark.createDataFrame([('Hello', 1), ('World', 2)], ["word", "count"])
df.show()

spark.stop()