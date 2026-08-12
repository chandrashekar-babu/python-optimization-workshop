from gevent import monkey; monkey.patch_all()

from threading import Thread
import itertools
from time import sleep

def testfn():
    sleep(60)

if __name__ == '__main__':
    for i in itertools.count():
        t = Thread(target=testfn)
        t.start()
        print(f"Created {i} threads: {t.name}")


