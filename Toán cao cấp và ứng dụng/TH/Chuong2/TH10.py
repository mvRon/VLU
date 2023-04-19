from sympy import Derivative, Symbol, sin, cos 
x1 = Symbol("x")
f1 = sin(2*x1)
print(Derivative(f1,x1).doit())

x2 = Symbol("x2")
f2 = sin(x2)*cos(x2)
print(Derivative(f2,x2).doit())