# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:55:55 2023

@author: dlewi
"""

import numpy as np
import matplotlib.pyplot as plt
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
    return x**(3/2)*y**(3/2)*np.sqrt((np.sin(alpha))/(2*y+x))



def velocity_of_river(y,x,alpha):
    '''
    Same as above, except does have area element so gives just the velocity 
    of the wave
    it is also mulipled by f/g ^1/2
    '''
    
    return (f/g)**(1/2)*x**(1/2)*y**(1/2)*np.sqrt((np.sin(alpha))/(2*y+x))
    

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
    
    
    
    k= np.zeros(len(y))
    #print(t)
    for i in range(len(y)):
        if i>0:
            k[i]=((g/f)**(1/2))*(-Q(y[i],5,alpha)+Q(y[i-1],5,alpha))
        else:
            k[i]=0
    #print(k[500],y[500])
    return k



#CLASSICAL CONSTANTS
g =9.81# accleration due to gravity
f =0.01# frictional factor
alpha=np.pi/10#angle of river


# l CONTROLS WHERE EVERYTHING APPEARS ON THE AXIS
l= 200 # number of volume elements 
y0=np.ones(l) #seting itnial values

length_of_river = 10 # total length of river we are evaluating in
x = np.linspace(0, length_of_river, l) #holds the guess of the points down the river
#if we make this close to height, pattern looks a lot more intersting
#y0[0] = 1.1  #setting inita left hand side



for a in range(0, 10):
    '''
    This sets the inital conditions to be not just a heavisde function
    meaning that there is a drop between
    '''
    y0[a] = 1 + (10-a)/500

#print(y0)




#TIME VARIABLES
final_time = 0.9
time_spaces = 200  # how many time points we are iterating over
t=np.linspace(0, final_time , time_spaces) #time evaluation


time_range = (0, final_time)



#SOLVING THE PDE
sol= solve_ivp(devfunc, time_range, y0 , t_eval=t, args=[x,alpha,f,g]) #integrating

print(sol)



number_of_waves = 8  # number of time snaps we want to plot 
#ACTUAL VALUE IS THIS VALUE -1

#d = 0
#for j in range(len(x)):
#    
#  ooo = int( time_spaces / number_of_waves)
#  
#
#  plt.scatter(x[j],sol.y[j][ooo*d],c='b')#ploting the length along the river 
#  #agunst the height
#  plt. xlabel('x - down river')
#  plt. ylabel ('height of river or area, unsure')
#  
#  plt.title('a variety of differnt cross sections of the river at different time')
#  plt.show()
#  
#  
  
  

for d in range(0, number_of_waves):
    for j in range(len(x)):
        
      ooo = int( time_spaces / number_of_waves)
      

      plt.scatter(x[j],sol.y[j][ooo*d],c='b')#ploting the length along the river 
      #agunst the height
      plt. xlabel('x - down river')
      plt. ylabel ('height of river or area, unsure')
      
      plt.title('a variety of differnt cross sections of the river at different time')
      plt.show()
      
      
      
      
      
      
      
      


   
   
   
   