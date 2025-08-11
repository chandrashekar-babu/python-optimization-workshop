from threading import Thread
from time import sleep

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        sleep(5)
       

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        if i > 5:
            while True: pass
        sleep(5)

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    