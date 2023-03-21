# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:36:35 2023

@author: dlewi
"""

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
        if i>=0:
            k[i]=((g/f)**(1/2))*(-Q(y[i],5,alpha)+Q(y[i-1],5,alpha))
        else:
            k[i]=0
    #print(k[500],y[500])
    return k

xmin = -2
xmax =15

#800
l=800# the amount of volume elements 
y0=np.ones(l)#seting itnial values
g=9.81# accleration due to gravity
f=0.01# frictional factor
x=np.linspace(xmin,xmax,l) #holds the guess of the points down the river

#lowcon = 0.02




#for a in range(0, l):

inlet_condition = 0.1
D= 1
    
y0=  D*np.exp(-(x)**2) + inlet_condition
#print(y0)
#
#for i in range(0, l):
#    if i > 50:
#        y0[i] = y0[i] - lowcon
        
        
        
t=np.linspace(0, 6, 100)#time evaluation
alpha=np.pi/10#angle
sol= solve_ivp(devfunc,[0,15],y0,t_eval=t,args=[x,alpha,f,g])#integrating




def update2d(frame, ax, line, xdata, ydata, tdata, anim=False):
    if line is None:
        line, = ax.plot(xdata, ydata[frame, :])
    line.set_data(xdata, ydata[frame, :])
    ax.set_title(f"time={tdata[frame]:.3f}")
    return line,



#
#def find_nearest(array, value):
#    array = np.asarray(array)
#    idx = (np.abs(array - value)).argmin()
#    #return array[idx]
#    #all we actually want is index
#    return idx


N = len(t)
y=sol.y
y = y.transpose()


mx_area = np.zeros(100)
mx_space = np.zeros(100)

for d in range(0, 100):
    mx_area[d] = np.amax(y[d])
    mx_space[d] = np.argmax(y[d])*17/800 -2
    
    ppp = find_nearest(y[d], 0.09)
    print(ppp)
 
    
    
print(mx_area)
print(mx_space)


#
#def closest_value(input_list, input_value):
# 
#  difference = lambda input_list : abs(input_list - input_value)
# 
#  res = min(input_list, key=difference)
# 
#  return res
# 
#if __name__ == "__main__" :
# 
#  list1 = y[d]
# 
#  num=int(input("Enter the value: "))
# 
#  val=closest_value(list1,num)
# 
#  print("The closest value to the "+ str(num)+" is",val)
#




#gives the peak value
max_value_twod_row = np.amax(y, axis = 1)
#max_value_twod_col = np.amax(numpy_twod_array, axis = 0)
#print("Row wise maximum: ", max_value_twod_row)

plt.plot(mx_space, max_value_twod_row)



"""
PLOTS FOR REPORT
"""


lin=np.linspace(1,l,l)
lin=lin/100

for i in range(len(sol.y[-1])):
   if i % 5==0:
      print(i,lin[i])
      plt.plot(x,sol.y[:,i])#ploting the length along the river agunst the hight
plt.title(f'f={f}')
plt.show()

















