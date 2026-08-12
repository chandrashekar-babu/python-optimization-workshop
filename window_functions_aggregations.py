from pyspark.sql import SparkSession

from pyspark.sql.window import Window
from pyspark.sql.functions import rank, desc

spark = SparkSession.builder.appName("AdvancedPythonTraining").getOrCreate()

# Mock dataset: Employees across departments
emp_data = [
    ("Finance", "Alice", 9000),
    ("Finance", "Bob", 12000),
    ("Tech", "Charlie", 15000),
    ("Tech", "David", 11000),
    ("Tech", "Eve", 15000)
]
emp_df = spark.createDataFrame(emp_data, ["department", "name", "salary"])

# 1. Standard GroupBy (Aggregation)
emp_df.groupBy("department").avg("salary").show()

# 2. Advanced Window Function: Rank salaries within each department
window_spec = Window.partitionBy("department").orderBy(desc("salary"))

ranked_df = emp_df.withColumn("salary_rank", rank().over(window_spec))
ranked_df.show()

