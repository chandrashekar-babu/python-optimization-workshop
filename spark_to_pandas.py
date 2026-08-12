from pyspark.sql import SparkSession
import pyspark.pandas as ps # Available in Spark 3.2+

spark = SparkSession.builder.appName("AdvancedPythonTraining").getOrCreate()

# 1. Enable PyArrow for optimization
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# 2. Use the Pandas API on Spark 
# This looks like Pandas, but scales across a cluster!
p_df = ps.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(type(p_df)) # <class 'pyspark.pandas.frame.DataFrame'>

# 3. Convert PySpark DataFrame to a true local Pandas DataFrame
spark_df = spark.createDataFrame([("Data1",), ("Data2",)], ["Column"])
local_pandas_df = spark_df.toPandas()

print(type(local_pandas_df)) # <class 'pandas.core.frame.DataFrame'>

