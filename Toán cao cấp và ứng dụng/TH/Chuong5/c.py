import sympy
from sympy import Derivative, Symbol, solve, pprint, sin, Integral, sqrt, Limit, S

# x = Symbol("x")
q = Symbol("q")
f = -0.8*q + 150
print("Dap an:", Integral(f, (q,0,25)).doit().evalf())
#cau 1
d = solve(-0.8*q + 150 - 5.2*q)
print(d)
print("Gia tri la:",f.subs({q:d[0]}).evalf())

#cau 2
tong_tien = Integral(f, (q,0,25)).doit().evalf() - f.subs({q:d[0]}).evalf()
print(f"Tong tien: {tong_tien}")

#cau 3
f1 = 5.2*q
a = 130*25 - Integral(f1, (q,0,25)).doit().evalf()
print("Kq = ",a)