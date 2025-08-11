# Install with pip install memory_profiler
from memory_profiler import profile

@profile
def process_large_dataset(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(parse_line(line))
    
    # Process the data
    result = [transform(item) for item in data]
    
    # Further operations
    return aggregate(result)