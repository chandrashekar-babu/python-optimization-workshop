# Install with pip install memory_profiler
from memory_profiler import profile

@profile
def generate_data(i):
    result = []
    for i in range(10_000):
        result.append(i)
    return result

def transform(v):
    return str(v)

@profile
def aggregate(data):
    result = ""
    for i in data:
        result += str(i)
    return len(result)

@profile
def process_large_dataset(howmany):
    data = []
    for i in range(howmany):
        data.append(generate_data(i))

    # Process the data
    result = [transform(item) for item in data]
   
    return aggregate(result)

if __name__ == '__main__':
    process_large_dataset(1000)
