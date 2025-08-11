from threading import Thread
from time import sleep

def testfn(name, count, delay):
    for i in range(count):
        print(f"testfn-{name}: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=testfn, args=("test-thread1", 10, 2))
    t2 = Thread(target=testfn, args=("test-thread2", 5, 2))
    t3 = Thread(target=testfn, args=("monitor", 40, 1), daemon=True)

    t1.start()
    t2.start()
    t3.start()
