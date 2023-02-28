import numpy as np
import matplotlib.pyplot as plt

# Define the problem parameters
gamma = 1.4  # specific heat ratio
L = 1.0  # length of the domain
N = 1000  # number of grid cells
dx = L / N  # grid spacing
x = np.linspace(0.0, L, N+1)  # grid points
t_final = 0.2  # final time
CFL = 0.8  # CFL number
rho_L = 1.0  # density on the left
rho_R = 0.125  # density on the right
u_L = 0.0  # velocity on the left
u_R = 0.0  # velocity on the right
p_L = 1.0  # pressure on the left
p_R = 0.1  # pressure on the right

# Define the initial conditions
rho = np.zeros(N+1)
u = np.zeros(N+1)
p = np.zeros(N+1)
for i in range(N+1):
    if x[i] < L/2:
        rho[i] = rho_L
        u[i] = u_L
        p[i] = p_L
    else:
        rho[i] = rho_R
        u[i] = u_R
        p[i] = p_R

# Define the function to compute the flux
def flux(rho, u, p):
    E = p/(gamma-1) + 0.5*rho*u**2  # total energy
    F = np.zeros_like(rho)
    F[0] = rho*u
    F[1] = rho*u**2 + p
    F[2] = rho*u*E + u*p
    return F

# Define the time step
dt = CFL*dx / np.max(np.abs(u) + np.sqrt(gamma*p/rho))

# Define the loop over time
t = 0.0
while t < t_final:
    # Compute the time step
    dt = CFL*dx / np.max(np.abs(u) + np.sqrt(gamma*p/rho))
    if t + dt > t_final:
        dt = t_final - t
    
    # Compute the fluxes at the cell interfaces
    F = flux(rho, u, p)
    F_left = F[:, :-1]
    F_right = F[:, 1:]
    
    # Compute the maximum wave speeds
    c = np.sqrt(gamma*p/rho)
    u_max = np.max(np.abs(u) + c)
    
    # Compute the left and right states at the cell interfaces
    rho_left = rho[:, :-1]
    rho_right = rho[:, 1:]
    u_left = u[:, :-1]
    u_right = u[:, 1:]
    p_left = p[:, :-1]
    p_right = p[:, 1:]
    alpha = 0.5*(u_max - np.abs(u_left + u_right))  # the alpha parameter
    rho_star = 0.5*(rho_left + rho_right) - alpha*(rho_right - rho_left)
    u_star = 0.5*(u_left + u_right) - alpha*(p_right - p_left)/(rho_left + rho_right)
    p_star = 0.5*(p_left + p_right) - alpha*rho_star*(u_right - u_left)
    
    #
    # Compute the fluxes at the cell interfaces using the star states
    F_star_left = flux(rho_star, u_star, p_star)[:, :-1]
    F_star_right = flux(rho_star, u_star, p_star)[:, 1:]

    # Update the solution
    rho[:, 1:-1] -= dt/dx * (F_star_right - F_star_left)
    u[:, 1:-1] -= dt/dx * (F_star_right[:, :-1] - F_star_left[:, :-1]) / rho[:, :-2]
    p[:, 1:-1] -= dt/dx * (F_star_right[:, :-1] * u[:, :-2] - F_star_left[:, :-1] * u[:, 1:-1])

    # Apply the boundary conditions
    rho[:, 0] = rho_L
    u[:, 0] = u_L
    p[:, 0] = p_L
    rho[:, -1] = rho_R
    u[:, -1] = u_R
    p[:, -1] = p_R

    # Update the time
    t += dt
plt.figure()
plt.plot(x, rho[0], label='density')
plt.plot(x, u[0], label='velocity')
plt.plot(x, p[0], label='pressure')
plt.legend()
plt.show()
