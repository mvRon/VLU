import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, sin, pi, plot
import math

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel("Truc X")
    plt.ylabel("Truc Y")
    plt.title("DO thi bai toan nem qua bong")


def frange(start, final, interval):
    number = []
    while start<final:
        number.append(start)
        start += interval
    return number


def draw_trajectory(u, theta):
    #gia toc trong truong
    g = 9.8

    #Goc bay
    theta = math.radians(theta)
    #thoi gian bay
    t_flight = 2*u*math.sin(theta)/g
    intervals = frange(0, t_flight, 0.001) 
    #danh sach toa do x va y
    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x,y)


u = float(input("Nhap van toc ban dau (m/s):"))
theta = float(input("Nhap goc bay (degrees):"))
draw_trajectory(u, theta)
plt.show()