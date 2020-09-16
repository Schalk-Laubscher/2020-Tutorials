import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Set up our constants
L  = 11
T  = 10  # Final time; not described in Worksheet
c  = 1
u0 = 1

dx = 1
dt = .25

# Create out arrays
nx = int(L // dx) + 1

current_temperature = np.zeros(nx)

# Create the initial data structure
for n in range(nx):
    x = n * dx
    if x < L/2:
        current_temperature[n] = 2*u0/L * x
    else:
        current_temperature[n] = 2*u0/L * (L-x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X_array, T_array = np.meshgrid(
    np.arange(0, L+dx, step=dx),
    np.arange(0, T+dt, step=dt)
)

recording = []

# Propogate the diffusion equation through time
nt = int(T // dt) + 1
for t in range(nt):
    next_temperature = np.zeros(nx)

    for i in range(1, nx-1):
        second_deriv = (
            current_temperature[i+1]
            - 2*current_temperature[i]
            + current_temperature[i-1]
        ) / dx**2

        next_temperature[i] = (
            current_temperature[i]
            + dt * c**2 * second_deriv
        )

    # Apply boundary conditions
    next_temperature[0] = (4*next_temperature[1] - next_temperature[2]) / 3
    next_temperature[nx-1] = (
        4*next_temperature[nx-2] - next_temperature[nx-3]) / 3

    current_temperature = next_temperature.copy()
    recording.append(current_temperature)

ax.plot_surface(X_array, T_array, np.array(recording))
plt.show()
