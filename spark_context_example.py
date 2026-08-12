from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Create a SparkConf object to configure the app
conf = SparkConf().setAppName("MyApp").setMaster("local[4]")

# Create a SparkContext
sc = SparkContext(conf=conf)

# Create an RDD (Resilient Distributed Dataset) from a list
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Process the RDD
squared = rdd.map(lambda x: x * x)
print(squared.collect()) # [1, 4, 9, 16, 25]

# Stop the context when done
sc.stop()