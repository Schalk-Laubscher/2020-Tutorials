# -*- coding: utf-8 -*-
"""
Week 4 ICT Session
"""

import numpy as np
from scipy import fft  # Import the module, NOT the function
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator


def mapping(x, xp, fp):
    """One dimensional linear mapping"""
    xmin, xmax = xp
    fmin, fmax = fp
    slope = (fmax - fmin) / (xmax - xmin)
    return (x - xmin) * slope + fmin


def approx(func, fit=(0, np.pi), num=50, plot=[5, 21], parity='odd'):
    """Approximate a function with a sum of sines.

    The given function is approximated using a discrete sine transform over the
    `fit` domain. The result is then shown over a domain of [-2pi, +2pi], using
    the `plot` number of terms.

    Parameters
    ----------
    func : callable
        A single parameter function to be fit
    fit : tuple, optional
        The domain to approximate the function over, by default (0, np.pi)
    num : int, optional
        The number of points to approximate over, by default 50
    plot : list, optional
        The number of terms to plot, by default [5, 21]
    """
    domain  = np.linspace(*fit, num=num)
    display = np.linspace(-2*np.pi, 2*np.pi, num=500)

    fourier = fft.dct if parity == 'even' else fft.dst
    trig    = np.cos if parity == 'even' else np.sin

    coeffs = fourier(func(domain))

    fig, ax = plt.subplots()
    ax.plot(display, func(display), 'k--')

    summation = 0.0
    for n, a in enumerate(coeffs, 0 if parity == 'even' else 1):
        if n == 0:
            a /= 2
        summation += trig(n*display) * a / num
        if n in plot:
            ax.plot(display, summation, label=f'N={n} terms')

    ax.legend()
    ax.xaxis.set_major_formatter(FuncFormatter(
        lambda val, _: f'{val/np.pi:.0g}$\pi$' if val else '0'  # noqa: W605
    ))
    ax.xaxis.set_minor_locator(MultipleLocator(base=np.pi/4))
    ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
    ax.set_xlim([-2*np.pi, 2*np.pi])

    plt.show()


if __name__ == '__main__':

    approx(lambda x: np.ones_like(x))
    approx(lambda x: x**2, parity='even')
    approx(lambda x: x, parity='odd')
