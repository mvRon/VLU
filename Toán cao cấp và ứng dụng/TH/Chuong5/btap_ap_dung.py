import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit, S
from sympy.plotting import plot

x = Symbol("x")
f = 2*x**3 - 9*x**2 + 12*x - 4
d = Derivative(f,x).doit()
cuc_tri = solve(d)
print("Gioi han cua ham so:", Limit(f, x, S.Infinity).doit())
print(f"Dao ham cua ham so tren: {d}")
print("Cuc tri cua ham so:", cuc_tri)
plot(f,(x, 1,2))


A = cuc_tri[0]
B = cuc_tri[1]
print(" Gia tri ham tai cuc tri: ",f.subs({x:A}).evalf())
print(" Gia tri ham tai x_min: ",f.subs({x:B}).evalf())


d2 = Derivative(d, x).doit()
print("Dao ham cap 2:", d2)
diem_uong = solve(d2)
print("Diem uon:", diem_uong)