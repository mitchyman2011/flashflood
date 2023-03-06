import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import quad
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

def AreaQuad(y,x):
    
    """This defines the area of a quadrolatral
            Parameters:
                    x (float): width of river (assumed constant)
                    y (float): height of river
            Returns:
                    The area of the quadralateral section"""
    return y*x
#    return (s**2)*t
def LengthSquare(A,x):
    return(2*A/x+x)


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

def AreaEllipse(r_1, r_2, theta_1, theta_2):
    """
    This defines the area of an ellipse

    Parameters
    ----------
    r_1 : FLOAT
        Major axis of ellipse.
    r_2 : FLOAT
        Minor axis of ellipse.
    theta_1 : FLOAT
        Angle between major axis and the height of the river measured from centre of ellipse.
    theta_2 : FLOAT
        Angle between the river height measured from centre of ellipse.

    Returns
    -------
    FLOAT
        Riverbed of an ellipse.

    """
    return 0.5*r_1*r_2*(theta_2-theta_1-np.sin(theta_2-theta_1))

def dL_dthet_Ellipse(r_1, r_2, theta):
    return np.sqrt(r_1**2*np.cos(theta)**2+r_2**2*np.sin(theta)**2)

def LengthEllipse():
    return 


#ls,hs = np.mgrid[slice(0.1,5,0.1),
#                slice(0.1,2,0.1)]
#us = u(np.pi/9,ls,hs,0.02)
#print(us)"""
