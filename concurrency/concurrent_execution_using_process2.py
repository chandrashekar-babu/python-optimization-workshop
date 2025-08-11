from multiprocessing import Process
from time import sleep

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        sleep(1)

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        sleep(1)

if __name__ == '__main__':
    t1 = Process(target=foo)
    t2 = Process(target=bar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    