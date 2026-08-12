from pyspark import SparkContext, SparkConf

# Configure and initialize SparkContext
conf = SparkConf().setAppName("WordCount").setMaster("local[*]")
sc = SparkContext(conf=conf)

# Load text file as RDD
lines = sc.textFile("shakespeare.txt")

# Transform the data: split into words, create (word, 1) pairs, count by key
words = lines.flatMap(lambda line: line.split(" "))

word_counts = words.map(lambda word: (word.lower(), 1)) \
    .reduceByKey(lambda a, b: a + b)

# Sort by count (descending)
sorted_counts = word_counts.map(lambda x: (x[1], x[0])) \
    .sortByKey(False) \
    .map(lambda x: (x[1], x[0]))

# Take the top 20 words

top_words = sorted_counts.take(20)

# Print the results
for word, count in top_words:
    print(f"{word}: {count}")

# Stop the SparkContext
sc.stop()