# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:02:13 2023

@author: dlewi
"""

"""
Spyder Editor
This is a temporary script file.
"""





import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#for square river
width = 1




#arbitarty constants to be used later
g = 9.81
friction =0.1 #friction factor
alpha = np.pi/5 #angle for river to flow

#SQUARE RIVER BED


#dA_i/dt = -(Q(A_i)-Q(A_(i-1))/dx




def Q(time, height):
    """
    Returns Q from equations (37)/(42) on notes
    Soley looking at a square river
    
    A is the Area of river bed filled with water
    t is time
    L is the length of river wetted and is a function of Area
    g & f are gravity and friction as defined above
    
    """
    
    #defined the area as fucntion of x and y. I asumassume this is for square river bet
    
    
    #varying the initail height as a fucntion of time
    
    
    Area = height*width    
    Length = width + 2*height
    
    '''
    Okay, so where is the t dependance, there is no t dependance, so solution gets 0 
    A should be a funtion of time ????
    
    '''
    
    #Yes this has time depenance
    
    return Area**(3/2)*np.sqrt((g*np.sin(alpha))/(friction*Length))




# f is the RHS of the above commented equation
def fdav(time, k):
    """
    RHS of the euqations
    """
    
    #picking an arbitary width of river
    
    height = 1 + np.sin(time)
    
    
    #I have removed height depenadnce as height is a fucntion of time for this
    return ((Q(k-1, height)-Q(k, height))/dx)



#size in x spacing
dx = 1/100





initial_height = 1 #+ 0.01*np.sin(time)

Q0 = Q(0, initial_height)
print(Q0, 'initial Q value')




A0 = initial_height * width
print(A0 , 'initial area')


#
#
##this seems to be working right
#sol = solve_ivp(fdav, time_range, [A0])
#plt.title('area of river at starting point, x =0')
#plt.ylabel('Area')
#plt.xlabel('Time')
#plt.plot(sol.t,sol.y[0])
#print(sol)



"""
Now we can express (37) as d/dt (A) + d/ds (Q) = 0
"""





#spacing jazz
x0 = 0
xn = 10

space_N = 3
dx = (xn - x0)/space_N

space_range = [x0, xn]
time_N = 3

#an empty set, length N
sols = np.zeros((time_N, space_N + 1))


final_time = 45



sols[0][1] =  A0 

#this gets an initial flow on the river of 0.1  before was, dunno why just added it
for i in range(2, space_N+1):
    sols[0][i] = 0.1

print(sols)

#TIME
for t in range(1,time_N):

    
    #2 numbers, initial and final time that solve ivp will work over. Nothing more
    time_range = [0, final_time]
    

    
    #gives collum 1, ie time
    sols[t][0] = final_time * t/ time_N
    
    
    
    #sol = solve_ivp(fdav, time_range, [sols[1][i-1]], args=[i])
    
    #this means the same amount of water flows in at a contant time
    sols[t][1] = 1
    
    individual_time_range = [sols[t-1][0], sols[t][0]]
    

    #sol = solve_ivp(fdav, individual_time_range, [sols[i - 1 ][2]], args=[i])

    
    
    #SPACE
    for x in range(1, space_N ):
        sol = solve_ivp(fdav, individual_time_range, [sols[t - 1 ][x]])
        #print(sol.y[1])
        #print(sol.y[0][0], 'f')
        
        
        sols[t][x+1] = sol.y[0][t]
        #print(sol)
        
#        print(sol.t, 't sol at ',i,  j)
#        print(sol.y, 'ysol at', i, j)
#        
#        print(sols[i][j], 'what is happening to data')
        
        #moves to next space block in the same time
        x = x+1
    
    

    
    #iterates next time loop
    t = t + 1

print(sols)













        
    