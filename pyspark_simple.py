from pyspark.sql import SparkSession

# 1. Create a Spark session
spark = SparkSession.builder.appName("BasicApp").getOrCreate()

# Suppress everything except actual compilation or runtime errors
spark.sparkContext.setLogLevel("ERROR")

# 2. Load data from a CSV file
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# 3. Transform and show data
df.filter(df["quantity"] > 25).select("product", "price").show()

# 4. Stop the session
spark.stop()

