# author: Rowan Gollan
# date: 20 Oct 2020

import numpy as np
from matplotlib.pyplot import contourf, contour, clabel, show

# problem set up
L = 3
H = 2
m = 11
n = 6
dx = L/(m-1)
dy = H/(n-1)

# set up a representation of the grid
x = np.linspace(0, L, m)
y = np.linspace(0, H, n)

# Set up boundary conditions


def Tn(x):
    return 8.0


def Te(y):
    return y*y*y


def Ts(x):
    return 0.0


def Tw(y):
    return 4.0*y


# 1. Assemble matrix
# Set up the coefficients
C0 = 1.0/(dx*dx)
C1 = -2.0/(dx*dx) - 2.0/(dy*dy)
C2 = 1.0/(dy*dy)

nNodes = m*n
A = np.zeros((nNodes, nNodes))
b = np.zeros((nNodes, 1))


def ij2p(i, j):
    return i + j*m


# 1a. assemble entries in interior nodes
for i in range(1, m-1):
    for j in range(1, n-1):
        # Select the row we're working on
        p = ij2p(i, j)
        # Set known value
        b[p] = 0.0
        # Set coefficients
        q = ij2p(i-1, j)
        A[p, q] = C0
        q = ij2p(i, j)
        A[p, q] = C1
        q = ij2p(i+1, j)
        A[p, q] = C0
        q = ij2p(i, j-1)
        A[p, q] = C2
        q = ij2p(i, j+1)
        A[p, q] = C2

# 1b. Set entries related to boundary conditions
# north
j = n - 1
for i in range(m):
    p = ij2p(i, j)
    b[p] = Tn(x[i])
    A[p, p] = 1.0
# east
i = m - 1
for j in range(n):
    p = ij2p(i, j)
    b[p] = Te(y[j])
    A[p, p] = 1.0
# south
j = 0
for i in range(m):
    p = ij2p(i, j)
    b[p] = Ts(x[i])
    A[p, p] = 1.0
# west
i = 0
for j in range(n):
    p = ij2p(i, j)
    b[p] = Tw(y[j])
    A[p, p] = 1.0

# 2. solve the equation
T = np.linalg.solve(A, b)

# 3. Plot the result as a contour
Tplot = np.ndarray.reshape(T, (n, m))

contourf(x, y, Tplot, 20)
cs = contour(x, y, Tplot, 10, linewidths=2, colors="black")
clabel(cs, inline=1)
show()
