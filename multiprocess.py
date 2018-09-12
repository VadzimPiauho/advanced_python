import multiprocessing
import time

DATA = 100


def list_data():
    for i in range(DATA + 1):
        yield i


def print_numbers(item):
    print("{}: {}".format(multiprocessing.current_process(), item))
    time.sleep(0.05)


pool = multiprocessing.Pool(2)

for item in list_data():
    pool.map(print_numbers, [item])

pool.close()
pool.join()
