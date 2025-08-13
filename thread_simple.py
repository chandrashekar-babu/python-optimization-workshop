#from threading import Thread, current_thread as current
from multiprocessing import Process as Thread, current_process as current

from time import sleep

def testfn(count, delay):
    t = current()

    for i in range(count):
        print(f"{t.name}: Counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=testfn, args=(10, 1), daemon=True)
    t2 = Thread(target=testfn, args=(5, 1))
    #t1.daemon = True
    t1.start()
    t2.start()
    testfn(3, 1)

    t2.join()
