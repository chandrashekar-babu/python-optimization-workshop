from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
.appName("MyApp") \
.master("local[4]") \
.config("spark.executor.memory", "2g") \
.getOrCreate()

# Get the underlying SparkContext if needed
sc = spark.sparkContext

# Create a DataFrame
df = spark.createDataFrame([
(1, "John", 25),
(2, "Alice", 30),
(3, "Bob", 35)
], ["id", "name", "age"])

# Show the DataFrame
df.show()

# Access Spark SQL functionality
df.createOrReplaceTempView("people")
results = spark.sql("SELECT * FROM people WHERE age > 25")
results.show()

# Stop the session when done
spark.stop()