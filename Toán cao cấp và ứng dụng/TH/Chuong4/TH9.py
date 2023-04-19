from sympy import Integral, Symbol
x = Symbol("x")
k = Symbol("k")
print(Integral(k*x,x).doit())