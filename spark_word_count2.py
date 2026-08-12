import re
from pyspark import SparkConf, SparkContext

# Initialize Spark Context
conf = SparkConf().setAppName("ShakespeareWordCount").setMaster("local[*]")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")  # Set log level to reduce verbosity

# 1. Load the text file into an RDD
lines_rdd = sc.textFile("shakespeare.txt")

# 2. Clean, tokenize, and count words
word_counts_rdd = (
    lines_rdd
    # Split lines into words, strip punctuation, and convert to lowercase
    .flatMap(lambda line: re.findall(r'[a-zA-Z\']+', line.lower()))
    # Map each word to a (word, 1) key-value pair
    .map(lambda word: (word, 1))
    # Reduce by key to sum up the frequencies
    .reduceByKey(lambda a, b: a + b)
    # Sort the results by count in descending order
    .sortBy(lambda pair: pair[1], ascending=False)
)

# 3. Print the top 10 most frequent words
print("\n--- TOP 10 FREQUENT WORDS ---")
for word, count in word_counts_rdd.take(10):
    print(f"{word}: {count}")

# Stop the Spark Context
sc.stop()
