from gevent import monkey; monkey.patch_all()

from concurrent.futures import ThreadPoolExecutor
from time import time

def slow_square(x):
    from time import sleep
    sleep(1)
    return x*x

#result = map(slow_square, list(range(10)))
#print(list(result))

start = time()

with ThreadPoolExecutor(max_workers=10) as executor:
    result = executor.map(slow_square, list(range(10)))
    print(list(result))

duration = time() - start
print("Duration: ", duration, "seconds")

