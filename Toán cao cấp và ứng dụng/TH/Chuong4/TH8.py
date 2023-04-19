import scipy 
from sympy import * 
import sys 
sys.displayhook = pprint 
x = Symbol('x') 
bt1 = integrate(x**2 + x + 1, x) 
pprint (bt1) 
bt2 = integrate(x/(x**2+2*x+1), x) 
pprint (bt2) 
bt3 = integrate(x**2 * exp(x) * cos(x), x) 
pprint (bt3) 
bt4 = integrate(exp(-x**2)*erf(x), x) 
pprint (bt4)