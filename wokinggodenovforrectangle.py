import numpy as np
import matplotlib.pyplot as plt
import scipy
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
def devfunc(t,y,x,alpha,f,g):
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
l=800# the amount of volume elements 
y0=np.ones(l)#seting itnial values
g=9.81# accleration due to gravity
f=0.1# frictional factor
x=np.linspace(0,2,l)#holds the guess of the points down the river
y0[0]=3#setting inita left hand side
t=np.linspace(0,2,50)#time evaluation
lin=np.linspace(1,l,l)
lin=lin/100
alpha=np.pi/10#angle
sol=scipy.integrate.solve_ivp(devfunc,[0,100],y0,t_eval=t,args=[x,alpha,f,g])#integrating
for i in range(len(sol.y[-1])):
   if i % 5==0:
      print(i,lin[i])
      plt.plot(x,sol.y[:,i])#ploting the length along the river agunst the hight
plt.title(f'f={f}')
plt.show()