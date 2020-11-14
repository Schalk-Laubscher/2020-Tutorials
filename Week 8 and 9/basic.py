import numpy as np
import matplotlib.pyplot as plt

TOL = np.finfo(float).resolution

# Set up our constants
Lx = 10 * 0.01   # [m]
Ly = 7.5 * 0.01  # [m]

rho = 7860  # [kg/m^3]
c_p = 490   # [J/kg.K]
k   = 54    # [W/m.K]

alpha = k / (c_p * rho)  # [m^2/s]

dx = 2.5 * 0.01  # [m]
dy = 2.5 * 0.01  # [m]
dt = 100

sigma_x = alpha * dt / dx**2
sigma_y = alpha * dt / dy**2

# Create out arrays
nx = int((Lx+TOL) // dx) + 1
ny = int((Ly+TOL) // dy) + 1  # NOTE: Tolerance for floating point error

# Dividing small floating point numbers sometimes doesn't give the expected
# answer. For example, 0.075 / 0.025 = 2.9999999999999996
# Without the tolerance, this gives ny = 3 rather than the expected 4.

# Configure initial conditions
current_temperature = (50+273.15) * np.ones(ny*nx)

# Configure boundary conditions
bottom_edge = np.array([110, 100, 90, 80, 70]) + 273.15
top_edge    = np.array([0, 10, 20, 30, 40]) + 273.15

left_edge  = np.array([65, 25]) + 273.15
right_edge = np.array([60, 50]) + 273.15

current_temperature[:nx] = bottom_edge
current_temperature[nx*(ny-1):] = top_edge

current_temperature[nx:3*nx:nx] = left_edge
current_temperature[2*nx-1:4*nx-1:nx] = right_edge

recording = []

implicit_matrix = np.zeros((nx*ny, nx*ny))

for i in range(ny):
    for j in range(nx):
        s = i*nx + j

        # Skip updating boundary nodes
        if i == 0 or i == ny-1:
            implicit_matrix[s, s] = 1
            continue
        if j == 0 or j == nx-1:
            implicit_matrix[s, s] = 1
            continue

        implicit_matrix[s, s]    = (1 + 2*sigma_x + 2*sigma_y)
        implicit_matrix[s, s-1]  = -sigma_x
        implicit_matrix[s, s+1]  = -sigma_x
        implicit_matrix[s, s-nx] = -sigma_y
        implicit_matrix[s, s+nx] = -sigma_y

recording.append(current_temperature)

for _ in range(100):
    next_temperature = np.linalg.solve(implicit_matrix, current_temperature)
    current_temperature = next_temperature.copy()

    recording.append(current_temperature)

# plt.plot([t[12] for t in recording])
# plt.show()
