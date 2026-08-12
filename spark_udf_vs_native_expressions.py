from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, when
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("AdvancedPythonTraining").getOrCreate()

# Mock dataset: student scores
scores_df = spark.createDataFrame([
    ("Alice", 85), ("Bob", 42), ("Charlie", 95)
], ["name", "score"])

# Approach A: The PySpark Native Way (Highly Optimized in JVM)
native_df = scores_df.withColumn(
    "status", 
    when(col("score") >= 50, "Pass").otherwise("Fail")
)
native_df.show()

# Approach B: The Python UDF Way (Slower, serializes data back and forth)
def check_status(score):
    return "Pass" if score >= 50 else "Fail"

# Register the Python function as a Spark UDF
status_udf = udf(check_status, StringType())

udf_df = scores_df.withColumn("status", status_udf(col("score")))
udf_df.show()

