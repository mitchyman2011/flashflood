import numpy as np
import matplotlib.pyplot as plt
import scipy
def Q(t,y,x,alpha):
    
    return x**(3/2)*y**(3/2)*np.sqrt((np.sin(alpha))/(2*y+x))
def devfunc(t,y,x,alpha,f,g):
    k=np.zeros(len(y))
    #print(t)
    for i in range(len(y)):
        if i>0:
            k[i]=(-Q(t,y[i],5,alpha)+Q(t,y[i-1],5,alpha))
        else:
            k[i]=0
    #print(k[500],y[500])
    return k
l=50
y0=np.ones(l)
g=9.81
f=0.1
x=np.linspace(1,10,l)
y0[0]=3
t=np.linspace(0,15,100)
alpha=np.pi/10
sol=scipy.integrate.solve_ivp(devfunc,[0,15],y0,t_eval=t,args=[x,alpha,f,g])
for i in range(len(sol.y[-1])):
   for j in range(len(x)):
      plt.scatter(x[j],sol.y[j][i],c='b')
   plt.show()