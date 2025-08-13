from multiprocessing import Process, Manager, current_process as current
from multiprocessing.shared_memory import SharedMemory
#from threading import Thread as Process
from time import sleep



def foo(d):
    d[0] += 97 
    sleep(2)
    print(f"In foo: {d=}")

def bar(d):
    sleep(1)
    print(f"In bar: {d=}")
    d[:] = bytearray(b'New Data')

if __name__ == '__main__':
    m = SharedMemory(create=True, size=12)
    buffer = m.buf
    buffer[:] = bytearray(b"Hello World")

    #d = {"test": 0}


    p1 = Process(target=foo, args=(buffer,))
    p2 = Process(target=bar, args=(buffer,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
