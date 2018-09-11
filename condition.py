from threading import Thread, Condition
import time

DATA = 100


def list_data():
    for i in range(DATA+1):
        yield i


def print_numbers(name_thred, condition):
    for item in generator_data:
        time.sleep(0.05)
        with condition:
            print("{}: {}".format(name_thred, item))
            condition.notifyAll()
            if item < DATA:
                condition.wait()


condition = Condition()
generator_data = list_data()

t1 = Thread(target=print_numbers, args=("Thread-1", condition,))
t2 = Thread(target=print_numbers, args=("Thread-2", condition,))

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

print("Exiting Main Thread")
