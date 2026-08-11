from multiprocessing import Process, Manager, current_process as current
#from threading import Thread as Process
from time import sleep



def foo(d):
    d["test"] = 100
    sleep(2)
    print(f"In foo: {d['test']=}")

def bar(d):
    sleep(1)
    print(f"In bar: {d['test']=}")
    d["test"] += 50

if __name__ == '__main__':
    m = Manager()

    #d = {"test": 0}

    d = m.dict()
    d["test"] = 0

    p1 = Process(target=foo, args=(d,))
    p2 = Process(target=bar, args=(d,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
