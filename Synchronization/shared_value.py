#from multiprocessing import Value
#from threading import Thread as Task
from multiprocessing import Process as Task, Value

from time import sleep


#class Value:
#    def __init__(self, ctype, value):
#        self.ctype = ctype
#        self.value = value

v = Value("i", 100)

def change_value(v):
    sleep(1)
    print(f"In change_value: v = {v.value}")
    v.value = 200
    print(f"In change_value: v changed to {v.value}")

def show_value(v):
    print(f"In show_value: v = {v.value}")
    sleep(2)
    print(f"In show_value: v now is {v.value}")

if __name__ == '__main__':
    t1 = Task(target=change_value, args=(v,))
    t2 = Task(target=show_value, args=(v,))

    t1.start()
    t2.start()
