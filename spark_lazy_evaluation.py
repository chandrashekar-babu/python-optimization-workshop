from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("AdvancedPythonTraining").getOrCreate()

# 1. Create a large mock DataFrame
data = [{"id": i, "value": i * 2} for i in range(10_000_000)]
df = spark.createDataFrame(data)

# 2. Define Transformations (Lazy - executes instantly, zero CPU usage)
start_time = time.time()
transformed_df = df.filter(df["id"] % 2 == 0).withColumn("triple_val", df["value"] * 3)
print(f"Transformations defined in: {time.time() - start_time:.4f} seconds") 

# 3. Trigger an Action (Eager - Spark optimizes the plan and processes data now)
start_time = time.time()
result_count = transformed_df.count()
print(f"Action executed in: {time.time() - start_time:.4f} seconds")
print(f"Total rows matching criteria: {result_count}")

