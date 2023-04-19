import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit
from sympy.plotting import plot

x = Symbol("x")
c = Symbol("c")
delta = Symbol("delta")
f = x * sin(1/x)
c = 0
delta = 1/4
print(Limit(f, x, 0, dir = '+'))
print(Limit(f, x, 0).doit())

sympy.plot(f, (x, c - delta, c + delta))
