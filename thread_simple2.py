from threading import Thread, current_thread

def counter(count, delay):
    th = current_thread()
    from time import sleep
    for i in range(count):
        print(f"thread {th.name}: Counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=counter, args=(10, 1))
    t2 = Thread(target=counter, args=(20, 1))

    t1.start()
    t2.start()

    counter(5, 1)
    print("main thread is complete.")

