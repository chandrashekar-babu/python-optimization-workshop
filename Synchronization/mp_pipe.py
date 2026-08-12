from multiprocessing import Process, Pipe

a = 100
b = [1, 2, 3, 4]
c = "hello world"
d = {"x": 100, "y": 200}


read_end, write_end = Pipe()

def sender(p):
    for v in a, b, c, d:
        p.send(v)
        print(f"Sent {v}")

def receiver(p):
    for i in range(4):
        data = p.recv()
        print(f"Received {data}")


if __name__ == '__main__':
    p1 = Process(target=sender, args=(write_end,))
    p2 = Process(target=receiver, args=(read_end,))
    p1.start()
    p2.start()
    