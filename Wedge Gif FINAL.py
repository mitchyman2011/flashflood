# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:51:11 2023

@author: dlewi


WEDGEEEEEE
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import functools
from scipy.integrate import solve_ivp




def AreaWedge(theta_1,theta_2,y):
    """
    This defines the area of a triangular wedge
    Parameters
    ----------
    theta_1 : FLOAT
        Left incline angle of river bed to perpendicular.
    theta_2 : FLOAT
        Right incline angle of river bed to perpendicular.
    y : FLOAT
        Height of river.
    Returns
    -------
    FLOAT
        Area of a triangular wedge.
    """
    return 0.5*(np.tan(theta_1)+np.tan(theta_2))*(y**2)


           
def LengthWedge(theta_1,theta_2,y):
    """
    This defines the riverbed length of a triangular wedge
    Parameters
    ----------
    theta_1 : FLOAT
        Left incline angle of river bed to perpendicular.
    theta_2 : FLOAT
        Right incline angle of river bed to perpendicular.
    y : FLOAT
        Height of river.
    Returns
    -------
    FLOAT
        Riverbed of a triangular wedge.
    """
    return y*(np.sqrt(np.tan(theta_1)+1)+np.sqrt(np.tan(theta_2)+1))



theta_1 = np.pi / 2.5
theta_2 = np.pi / 4




def Q(y,x,alpha):
    '''
    Returns the flux of a volume elemnent in the s direction
          Parameters:
                  y (float): the current hight of this element of the river
                  x (float):the current width of this element of the river
                  alpha(float): the angle of the river reletive t the horisontal
          Returns:
                  Q (float): returns the value of Q
    '''
    Length = LengthWedge(theta_1,theta_2,y)
    Area = AreaWedge(theta_1,theta_2,y)
    return Area**(3/2)*np.sqrt((np.sin(alpha))/(Length))



def devfunc(t,y):
    '''
    Returns the value of the derivitive over time of the hight we requie the left side to never change so that is set to 0
          Parameters:
                  t(float): is the current time
                  y (float): the current hight of this element of the river
                  x (float):the current width of this element of the river
                  alpha(float): the angle of the river reletive t the horisontal
                  f(float): the frictional factor
                  g(float): the acleration due to gravity
          Returns:
                  k (float): returns the value of the time derivitive of the hight
    '''
    k=np.zeros(len(y))
    #print(t)
    for i in range(len(y)):
        if i>0:
            k[i]=((g/f)**(1/2))*(-Q(y[i],5,alpha)+Q(y[i-1],5,alpha))
        else:
            k[i]=0
    #print(k[500],y[500])
    return k



xmin = 0
xmax =15


l =800# the amount of volume elements 
y0 =np.ones(l)#seting itnial values
g =9.81# accleration due to gravity
f =0.01# frictional factor
x =np.linspace(xmin,xmax,l)#holds the guess of the points down the river







#for a in range(0, l):

inlet_condition = 0.1
D= 1
    
y0=  D*np.exp(-(x)**2) + inlet_condition
#print(y0)


t=np.linspace(0, 6, 100)#time evaluation
alpha=np.pi/10#angle
sol= solve_ivp(devfunc,[0,15],y0,t_eval=t)#,args=[x,alpha,f,g])#integrating




def update2d(frame, ax, line, xdata, ydata, tdata, anim=False):
    if line is None:
        line, = ax.plot(xdata, ydata[frame, :])
    line.set_data(xdata, ydata[frame, :])
    ax.set_title(f"time={tdata[frame]:.3f}")
    return line,


N = len(t)
y=sol.y
y = y.transpose()







'''
PLOTS
'''
fig, ax = plt.subplots()
ax.set_xlabel("x")
ax.set_xlim([xmin,xmax])

ax.set_ylabel("area")
ax.set_ylim([0,2.5])

line, = update2d(0, ax, None, x, y, t, True)
update_anim = functools.partial(update2d, ax=ax, line=line, 
                                xdata=x, ydata=y, tdata=t, anim=True)
ani = animation.FuncAnimation(fig, update_anim, N, interval=25, blit=False)
ani.save('test.gif')