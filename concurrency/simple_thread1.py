from threading import Thread
from time import sleep

def testfn(count=5, delay=1):
    print("testfn started....")
    for i in range(count):
        print(f"testfn: counting {i}")
        sleep(delay)

if __name__ == '__main__':
    #t = Thread(target=testfn)
    #t = Thread(target=testfn, args=(10, 0.2))
    #t = Thread(target=testfn, kwargs={"delay": .2})
    t = Thread(target=testfn, kwargs=dict(delay=0.2), name="heart-beat")
    print(t)
    print(t.name)

    t.start()
    t.join()
