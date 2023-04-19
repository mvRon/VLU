from sympy import Symbol, solve, Derivative 
x = Symbol('x') 
f = x**5-30*x**3+50*x 
d1 = Derivative(f, x).doit()
cuc_tri = solve(d1)
print(cuc_tri)
A = cuc_tri[0]
A = cuc_tri[2]
B = cuc_tri[0]
C = cuc_tri[1]
D = cuc_tri[3]
d2 = Derivative(d1,x,2).doit()
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:A}).evalf())
print(d2.subs({x:D}).evalf())

x_min = -5
x_max = 5
print(f.subs({x:A}).evalf())
print(f.subs({x:C}).evalf())
print(f.subs({x:x_min}).evalf())
print(f.subs({x:x_max}).evalf())
print(f.subs({x:B}).evalf())
print(f.subs({x:D}).evalf())

E = Symbol("E")
g = E**x
g1 = Derivative(g,x)
print(g1)
print(solve(g1))



