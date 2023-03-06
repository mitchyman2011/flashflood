# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
g = 9.81
f =0.1
alpha = np.pi/5

#Gudunov solution takes form dy_i/dt = -(Q(y_i)-Q(y_(i-1))/dx
#Q as a function of y for a rectangular river bed
def Q(t,y,x):
    return x**(3/2)*y**(3/2)*np.sqrt((np.sin(alpha))/(2*y+x))

# f is the RHS of the above commented equation
def f(t,y,i):
    return (Q(i-1,y,alpha)-Q(i,y,alpha))

"""Iterates over a range 0 to N solving the IVP, currently it iterates over some range i but 
it needs to be a bit more complicated than that, see page 24 of the notes for the correct 
implementation."""
def gudunov(N):
    sols = np.zeros(N)
    for i in range(1,N):
        y0 = [10]
        sol = solve_ivp(f,[0,10],y0,args=[i])
        i = i+1
        plt.plot(sol.t,sol.y[0])
    
    return sols

t=np.arange(100)
y= np.arange(100)
x = np.arange(10)

for i in x:
    qs = Q(t,y,i)
    plt.plot(qs)