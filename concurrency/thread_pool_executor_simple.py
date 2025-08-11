from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Processing {n}")
    time.sleep(1)  # Simulate I/O or computation
    return n * n

# Create a thread pool
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks and get Future objects
    futures = [executor.submit(task, i) for i in range(10)]
    
    # Wait for all tasks to complete and get results
    for future in futures:
        result = future.result()
        print(f"Result: {result}")