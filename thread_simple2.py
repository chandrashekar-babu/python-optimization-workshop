from threading import Thread, current_thread

def counter(count, delay):
    th = current_thread()
    from time import sleep
    for i in range(count):
        print(f"thread {th.name}: Counting {i}")
        sleep(delay)

if __name__ == '__main__':
    t1 = Thread(target=counter, args=(10, 1), name="Counter-Thread")
    t2 = Thread(target=counter, args=(20, 1), name="Test-Thread")

    t1.start()
    t2.start()

    counter(5, 1)
    t1.join()
    print("t1 completed.")

    t2.join()
    print("t2 completed.")

    print("main thread is complete.")

