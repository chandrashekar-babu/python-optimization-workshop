from gevent import monkey
monkey.patch_all()

from threading import Thread
from time import sleep

def testfn():
    for i in range(1000):
        print(i)
        sleep(0.5)

if __name__ == '__main__':
    threads = []
    for _ in range(10):
        t = Thread(target=testfn)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
