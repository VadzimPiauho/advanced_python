import sys
sys.setrecursionlimit(35000)
def f(f): return f(f)
f(f)