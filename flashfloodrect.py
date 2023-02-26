# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:33:03 2023

@author: cadol,mitchyman2011
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
                    l (func): it is a length as a function of the area
                    A (func): The area of the bed
                    f (float): frictional factor of the bed on the water
                    g (float): the accleration due to gravity
            Returns:
                    The average velocity of the river
   """
    u = np.sqrt(A*g*np.sin(alpha)/(f*l(A)))
    return u

def AreaSquare(s,t):
   return (s**2)*t
def LengthSquare(A):
    return(np.sqrt(A)*3)
def AreaWedge():

def LengthWedge():

def AreaParabola():

def LengthParabola():
#ls,hs = np.mgrid[slice(0.1,5,0.1),
#                slice(0.1,2,0.1)]

#us = u(np.pi/9,ls,hs,0.02)
#print(us)

