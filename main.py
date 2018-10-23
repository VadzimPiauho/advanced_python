from benchmark import Profiler

from fib_cython.fibonacci import fibonacci as fib_cython
from fib import fib_fast as fib_python_ext
from fib_python.fibonacci import fibonacci as fib_python


COUNT = 10

with Profiler() as p:
    # print("Python_fibonacci")
    fib_python(COUNT)

with Profiler() as p:
    # print("Cython_fibonacci")
    fib_cython(COUNT)

with Profiler() as p:
    # print("C Python_extension")
    fib_python_ext(COUNT)
