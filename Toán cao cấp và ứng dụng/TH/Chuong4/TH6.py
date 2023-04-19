hinhthang = lambda f,a,b: (b-a)*(f(a) + f(b))/2
from math import exp #ham e^x
print(hinhthang(exp,0,1))

def hai_x(x):
    return 2*x

print(hinhthang(hai_x, 1,2))