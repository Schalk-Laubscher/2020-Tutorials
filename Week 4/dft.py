# -*- coding: utf-8 -*-
"""
Week 4 ICT Session
"""

import numpy as np
from scipy import fft  # Import the module
import matplotlib.pyplot as plt


def function(x):
    return x


def approx(x, N):
    output = 0.0 
    for n in range(N):
        if n % 2 == 0:
            continue
                # Term n ->
        output += np.sin(n*x) * 4 / (np.pi * n)
    return output
        

if __name__ == '__main__':
    interval = np.linspace(-2*np.pi, 2*np.pi)
    plt.plot(interval, approx(interval, N=5), label='N=5')

    plt.plot(interval, approx(interval, N=21), label='N=21')
    plt.legend()
    plt.show()
    
    small_interval = np.linspace(0, np.pi)
    small_function = function(small_interval)
    coeffs = fft.fft(small_function)
    
    freq = fft.fftfreq(n=small_function.size)
    plt.figure()
    plt.plot(fft.ifftshift(freq), coeffs.real)
    plt.plot(fft.ifftshift(freq), coeffs.imag)
    
# =============================================================================
#     plt.figure()
#     plt.plot(small_interval, small_function, label='f(x)=x')
#     for N in [5, 21]:
#         recreation = fft.fft(coeffs[:N], n=small_function.size)
#         plt.plot(small_interval.real, recreation, label=f'N={N} approximation')
#     plt.legend()
# =============================================================================
    