from concurrent.futures import ProcessPoolExecutor as Executor
from time import sleep, time

def slow_square(x):
    sleep(1)
    return x*x


def busy_square(x):
    for _ in range(10**8):
        pass
    return x*x

if __name__ == '__main__':
    values = [3, 6, 8, 2, 1, 9, 5]

    start = time()
    result = list(map(busy_square, values))
    duration = time() - start

    print(f"{result=}, {duration=}")

    start = time()
    with Executor(max_workers=10) as workers:
        result = list(workers.map(busy_square, values))

    duration = time() - start

    print(f"{result=}, {duration=}")

