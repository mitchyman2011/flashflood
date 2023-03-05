# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
g = 9.81

def u(alpha,l,A,f):
   """
    This function returns the average speed of the river, this aproximation
    is used because turbulent flow is allmost uniform on large scales
            Parameters:
                    alpha (float): Angle of the fiver with respect to gravity
                    l (float): it is a length as a function of the area
                    A (float): The area of the bed
                    f (float): frictional factor of the bed on the water
                    g (float): the accleration due to gravity
            Returns:
                    The average velocity of the river
   """
   u =np.sqrt(A*g*np.sin(alpha)/(f*l))
   return u

def AreaQuad(s,t):
    
    """This defines the area of a quadrolatral
            Parameters:
                    s (float): length along the river
                    t (float): de time bro
            Returns:
                    The area of the quadralateral section"""

    return (s**2)*t
def LengthSquare(A):
    return(np.sqrt(A)*3)


def Q(s,alpha):
    return (5/2)*s**(3/2)*np.sqrt(np.sin(alpha))

def gudunov(N,s,L):
    sols = np.zeros(N)
    for i in range(1,N):
        f = Q(AreaQuad[i-1])-Q(AreaQuad[i])
        A0 = 0
        sol = solve_ivp(f,[0,100],A0)
        sols[i] = sol
        i = i+1
    
    return sol


"""def AreaWedge():

def LengthWedge():

def AreaParabola():

def LengthParabola():
#ls,hs = np.mgrid[slice(0.1,5,0.1),
#                slice(0.1,2,0.1)]

#us = u(np.pi/9,ls,hs,0.02)
#print(us)"""