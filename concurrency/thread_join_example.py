from threading import Thread
from time import sleep

def testfn(name, count, delay):
    for i in range(count):
        print(f"testfn-{name}: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t = Thread(target=testfn, args=("simple_thread", 3, 1))
    print("main: created a thread ", t)
    
    t.start()
    testfn("main", 5, 1)
    print("main: joining on", t.name)
    #t.join()  # Blocks the current thread indefinitely until thread 't' exits.
    t.join(timeout=10)
    if t.is_alive():
        print(f"Thread {t.name} is still alive")
    else:
        print(f"Thread {t.name} exited")
    print(f"main: {t.name} joined")

