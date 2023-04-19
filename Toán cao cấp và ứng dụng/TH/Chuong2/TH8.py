from sympy import Symbol, Derivative 
t = Symbol("t")
t1 = Symbol("t1")
t2 = Symbol("t2")
st = 5*t**2 + 2*t + 8
d = Derivative(st,t)
print(d.doit())
t2 = 10
print(d.doit().subs({t:1}))
print(d.doit().subs({t:t1}))
print(d.doit().subs({t:t2}))

