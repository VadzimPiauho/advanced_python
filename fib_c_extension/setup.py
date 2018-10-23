from distutils.core import setup, Extension

module1 = Extension('fib', sources=['fibmodule.c'])

setup(name='Fibonacci',
      version='1.0',
      description='Homework12',
      ext_modules=[module1])
