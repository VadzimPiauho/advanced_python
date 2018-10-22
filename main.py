from benchmark import Profiler
from counter import count_fib
from fib_python.fibonacci import fibonacci as fib_python
import fib_cython

COUNT = 100


with Profiler() as p:
    # print("Python_fibonacci")
    count_fib(fib_python, COUNT)

with Profiler() as p:
    # print("Cython_fibonacci")
    count_fib(fib_cython.fibonacci.fibonacci, COUNT)
