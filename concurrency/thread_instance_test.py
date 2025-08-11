from threading import Thread, current_thread as current, main_thread
from time import sleep

def counter(count, delay):
    t = current()
    for i in range(count):
        if t is main_thread():
            print(f"Running as main thread: counting {i}")
        else:
            print(f"counter[{t}]: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=counter, args=(10, 1))
    t2 = Thread(target=counter, args=(20, 0.5))

    t1.start()
    t2.start()

    counter(5, 2)

