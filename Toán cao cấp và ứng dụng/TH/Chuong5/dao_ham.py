import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit
from sympy.plotting import plot

x = Symbol("x")
f = -x**2 +4*x - 3
d1 = Derivative(f, x).doit()
cuc_tri = solve(d1)
print(cuc_tri)
# print(d1)

A = cuc_tri[0]
d2 = Derivative(d1, x).doit()
d2.subs({x:A}).evalf()
x_min = 0
x_max = 4
print(" Gia tri ham tai cuc tri: ",f.subs({x:A}).evalf())
print("Gia tri ham tai x_min:",f.subs({x:x_min}).evalf())
print("Gia tri ham tai x_max:",f.subs({x:x_max}).evalf())
print(d2)
plot(f, (x, 0, 4))
