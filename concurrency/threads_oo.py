from threading import Thread
from time import sleep

class Counter(Thread):

    def __init__(self, count=10, delay=1):
        super().__init__()
        # super(Counter, self).__init__()  # Python 3.0 to 3.3
        # Thread.__init__(self)  # Python 2.x
        self.count, self.delay = count, delay

    def run(self):
        for i in range(self.count):
            print(f"{self}: counting {i}")
            sleep(self.delay)

if __name__ == '__main__':
    c1 = Counter(count=5, delay=2)
    c2 = Counter(count=10, delay=1)

    c1.start()
    c2.start()

    c1.join()
    c2.join()