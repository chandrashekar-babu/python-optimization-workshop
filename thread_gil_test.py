from threading import Thread

def profile(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def cpu_bound_task():
    # Simulate a CPU-bound task
    count = 0
    for i in range(10**8):
        count += i
    return count

@profile
def run_sequential():
    for _ in range(4):
        cpu_bound_task()

@profile
def run_multithreaded():
    threads = []
    for _ in range(4):
        thread = Thread(target=cpu_bound_task)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_sequential()
    run_multithreaded()