# Install with pip install line_profiler
from line_profiler import profile

@profile
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

@profile
def transform(v):
    return v*v

@profile
def process_data(items):
    result = []
    for item in items:
        if is_prime(item):
            result.append(transform(item))
    return sorted(result)

data = list(range(1_000_000))
process_data(data)
    