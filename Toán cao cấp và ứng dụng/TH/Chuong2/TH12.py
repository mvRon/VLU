import sympy
from pylab import plot,show
x = sympy.Symbol("x")
f = x**5-30*x**3+50*x
sympy.plot(f,(x,-5,5))
show()
