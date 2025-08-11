from time import sleep

def testfn1():
    j = 0
    for i in range(100_000_000):
        j += i

def testfn2():
    j = 0
    for i in range(1_000_000):
        if i % 5 == 0:
            sleep(0.00001)
        j += i


if __name__ == '__main__':
    testfn1()

