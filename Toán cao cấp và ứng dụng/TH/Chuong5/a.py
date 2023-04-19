import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit, S
from sympy.plotting import plot

x = Symbol("x")
a = Symbol("a")
f = -2*x**3 + 2*a*x
d1 = Derivative(f, x).doit()
d2 = solve(d1)
print(f"Cuc tri cua {d1}: {d2}")
x_1 = f.subs({x:0}).evalf()
x_2 = f.subs({x:sqrt(a)}).evalf()
x_3 = f.subs({x:sqrt(a/3)}).evalf()
print(f"x1 = {x_1}")
print(f"x2 = {x_2}")
print(f"x3 = {x_3}")




