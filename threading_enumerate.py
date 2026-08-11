import threading
from threading import Thread

def testfn():
    from time import sleep
    sleep(10)

for _ in range(12):
    Thread(target=testfn).start()

print(threading.enumerate())

for t in threading.enumerate():
    if t is not threading.main_thread():
        t.join()
        print(f"{t} complete.")
