import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as splinalg

TOL = np.finfo(float).resolution

# Set up our constants
Lx = 10 * 0.01   # [m]
Ly = 7.5 * 0.01  # [m]

rho = 7860  # [kg/m^3]
c_p = 490   # [J/kg.K]
k   = 54    # [W/m.K]

alpha = k / (c_p * rho)  # [m^2/s]

dx = 2.5 * 0.01 / 50  # [m]
dy = 2.5 * 0.01 / 50  # [m]
dt = 10

# Calculate the CFL numbers
sigma_x = alpha * dt / dx**2
sigma_y = alpha * dt / dy**2

# Create array sizes
nx = int((Lx+TOL) // dx) + 1
ny = int((Ly+TOL) // dy) + 1  # NOTE: Tolerance for floating point error

# Dividing small floating point numbers sometimes doesn't give the expected
# answer. For example, 0.075 / 0.025 = 2.9999999999999996
# Without the tolerance, this gives ny = 3 rather than the expected 4.

# Configure initial conditions
temperature = (50+273.15) * np.ones(ny*nx)

# Configure boundary conditions
bottom_edge = np.array([110, 100, 90, 80, 70]) + 273.15
top_edge    = np.array([0, 10, 20, 30, 40]) + 273.15

left_edge  = np.array([110, 65, 25, 0]) + 273.15
right_edge = np.array([70, 60, 50, 40]) + 273.15

# Interpolate the boundary conditions from given data
#
# np.linspace(0, 1, n<>) ->
#   Label the nodes of the new resolution from 0 to 1
#
# np.linspace(0, 1, <>_edge.size) ->
#   Label the known temperatures from 0 to 1
#

temperature[:nx] = np.interp(
    np.linspace(0, 1, nx),
    np.linspace(0, 1, bottom_edge.size),
    bottom_edge)
temperature[nx*(ny-1):] = np.interp(
    np.linspace(0, 1, nx),
    np.linspace(0, 1, top_edge.size),
    top_edge)

temperature[:ny*nx:nx] = np.interp(
    np.linspace(0, 1, ny),
    np.linspace(0, 1, left_edge.size),
    left_edge)
temperature[nx-1:(ny+1)*nx-1:nx] = np.interp(
    np.linspace(0, 1, ny),
    np.linspace(0, 1, right_edge.size),
    right_edge)

recording = []

# Construct the implicit matrix EFFICIENTLY.
# Use sps.eye to create scipy.sparse.dia_matrix
# which the most efficient storage for diagonal data

implicit_matrix = (
    (1 + 2*sigma_x + 2*sigma_y) * sps.eye(nx*ny, k=0)
    - sigma_x * sps.eye(nx*ny, k=+1)
    - sigma_x * sps.eye(nx*ny, k=-1)
    - sigma_y * sps.eye(nx*ny, k=+nx)
    - sigma_y * sps.eye(nx*ny, k=-nx)
)

# This double for loop is inefficient...
# Search for a better way!

for i in range(ny):
    for j in range(nx):
        s = i*nx + j

        # Set row to zero           -> Clear the "equation"
        # Set diagonal element to 1 -> next T = current T

        if i == 0 or i == ny-1:
            implicit_matrix[s, :] = 0
            implicit_matrix[s, s] = 1
        if j == 0 or j == nx-1:
            implicit_matrix[s, :] = 0
            implicit_matrix[s, s] = 1

# Show the implicit matrix, for sanity check
plt.matshow(implicit_matrix.toarray())
plt.show()


# Iterate over 100 time steps
for _ in range(100):
    # Use scipy.sparse.linalg.spsolve instead of numpy
    # (There are even more efficient ways...)
    temperature = splinalg.spsolve(implicit_matrix, temperature)
    recording.append(temperature)


# Plot a heatmap of the final temperature, for sanity check
plt.matshow(temperature.reshape((ny, nx)))
plt.gca().invert_yaxis()
plt.show()
