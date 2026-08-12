from threading import Thread, Event
from queue import Queue

class ThreadPool:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.workers = []
        self.queue = Queue(max_workers)
        self.quit = Event()

    def start(self):
        self.quit.clear()
        for _ in range(self.max_workers):
            t = Thread(target=self._wait_on_queue)
            t.start()
            self.workers.append(t)

    def _wait_on_queue(self):
        while not self.quit.is_set():
            task = self.queue.get()
            if task is None:
                continue
            else:
                task.run()

    def shutdown(self):
        self.quit.set()
        while not self.queue.full():
            self.queue.put(None)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, et, ev, tb):
        self.shutdown()


    def submit(self, fn, args=(), kwargs={}):
        task = Future(fn, args, kwargs)
        self.queue.put(task)
        task.status = "QUEUED"
        return task

class Future:
    def __init__(self, fn, args=(), kwargs={}):
        self.fn = fn
        self.fn_args = args
        self.fn_kwargs = kwargs
        self._result = None
        self.status = "INITIALIZED"
        self.completed = Event()

    def run(self):
        self.completed.clear()
        self.status = "RUNNING"
        self._result = self.fn(*self.fn_args, **self.fn_kwargs)
        self.status = "COMPLETED"
        self.completed.set()

    @property
    def result(self):
        self.completed.wait()
        return self._result
        
        

            