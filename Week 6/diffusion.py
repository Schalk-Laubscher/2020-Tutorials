import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


@np.vectorize
def func(x, t):
    """Return temperature distribution."""
    if 0 <= x < L/2:
        return 2*u0/L * x
    else:  # L/2 < x < L
        return 2*u0/L * (L-x)


if __name__ == '__main__':

    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')

    u0 = 1
    L  = 2
    t  = 3

    x_steps = 100
    t_steps = 200

    X_array, T_array = np.meshgrid(
        np.linspace(0, L, num=x_steps),
        np.linspace(0, t, num=t_steps)
    )
    U_array = func(X_array, T_array)

    ax.plot_surface(X_array, T_array, U_array)
    plt.show(block=True)
