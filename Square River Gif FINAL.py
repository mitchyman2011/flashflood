# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:31:23 2023

@author: dlewi
"""

#SQUARE RIVER BED

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

import functools
from scipy.integrate import solve_ivp


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
    Area = x*y
    
    Length = 2*y+x
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
            k[i]=((g/f)**(1/2))*(-Q(y[i],2,alpha)+Q(y[i-1],2,alpha))
        else:
            k[i]=0
    #print(k[500],y[500])
    
    return k
jeff=np.linspace(0.01,0.1,10)
for f in jeff:
    xmin = 0
    xmax =15
    f=round(f,3)

    l=800# the amount of volume elements 
    y0=np.ones(l)#seting itnial values
    g=9.81# accleration due to gravity
#f=0.01# frictional factor
    s=np.linspace(xmin,xmax,l)#holds the guess of the points down the river


#for a in range(0, 10):
#    '''
#    This sets the inital conditions to be not just a heavisde function
#    meaning that there is a drop between
#    '''
#    y0[a] = 1 + (10-a)/50
    

#for a in range(0, l):

    inlet_condition = 0.1
    D= 1
    k=1
    y0=  D*np.exp(-(k*s)**2) + inlet_condition
#print(y0)
    
   # print(1000*f)
    t=np.linspace(0, 30, 101)#time evaluation
    alpha=np.pi/12#angle
    x=2
    sol= solve_ivp(devfunc,[0,30],y0,t_eval=t) #,args=[x,alpha,f,g])#integrating


    N = len(t)
    y=sol.y
    y = y.transpose()







    fig, ax = plt.subplots()
    ax.set_xlabel("x")
    ax.set_xlim([xmin,xmax])

    ax.set_ylabel("Area")
    ax.set_ylim([0,2.5])

#line, = update2d(0, ax, None, s, y, t, True)
#update_anim = functools.partial(update2d, ax=ax, line=line, 
#                                xdata=s, ydata=y, tdata=t, anim=True)
#ani = animation.FuncAnimation(fig, update_anim, N, interval=25, blit=False)
#ani.save('test.gif')
    for i in range(len(sol.y[-1])):
        if i % 10==0:
            #print(i)
            b=sol.t[i]
            plt.plot(s,sol.y[:,i],label=f"t={b}")
    plt.ylabel("Area")
    plt.xlabel("s")
    plt.title(f"The wave progressing over time with frictional factor $f={f}$")
    plt.legend(ncol=3,loc=1)
    plt.savefig(f'data/frictionalfactor={f}.jpg')
   
def update2d(frame, ax, line, xdata, ydata, tdata, anim=False):
    if line is None:
        line, = ax.plot(xdata, ydata[frame, :])
    line.set_data(xdata, ydata[frame, :])
    ax.set_title(f"data/time={tdata[frame]:.3f}")
    return line,


