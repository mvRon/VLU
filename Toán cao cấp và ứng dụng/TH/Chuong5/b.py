import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit, S

x = Symbol("x")
f = -10*x**2 + 25000*x - 120000000
d = Derivative(f,x).doit()
cuc_tri = solve(d)
print(cuc_tri)

A = cuc_tri[0]
Max = f.subs({x:A}).evalf()
print(f"Loi nhuan toi da:", Max)