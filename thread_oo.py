from threading import Thread

class CounterThread(Thread):
    def __init__(self, count, delay):
        super().__init__() # super(CounterThread, self).__init__() # Thread.__init__(self)

        self.count, self.delay = count, delay

    def run(self):
        from time import sleep
        for i in range(self.count):
            print(f"{self.name}: Counting {i}")
            sleep(self.delay)
    
if __name__ == '__main__':
    t1 = CounterThread(10, 1)
    t2 = CounterThread(20, 0.5)
    t1.start()
    t2.start()
    