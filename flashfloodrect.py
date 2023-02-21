# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:33:03 2023

@author: cadol
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
g = 9.81

def u(alpha,l,h,f):
    A = l*h
    L= l+2*h
    u = np.sqrt(A*g*np.sin(alpha)/(f*L))
    return u 


ls,hs = np.mgrid[slice(0.1,5,0.1),
                 slice(0.1,2,0.1)]

us = u(np.pi/9,ls,hs,0.02)
print(us)