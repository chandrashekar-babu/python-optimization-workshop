from threading import Thread
from time import sleep

def foo():
    for i in range(10):
        print("foo: counting", i)
        sleep(1)

def bar():
    for i in range(10):
        print("bar: counting", i)
        sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    t1.start()
    t2.start()
    