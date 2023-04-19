import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, sin, pi, plot
import math

x = np.arange(100,1000,50)
m1 = 0.5
m2 = 1.5
G = 6.67 * 10**(-11)
f = (G*m1*m2)/x**2
plt.plot(x,f, marker = "o")
plt.show()
