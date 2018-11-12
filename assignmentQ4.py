#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:57:52 2018

@author: Tosca

Question 4: Fourier Transforms

"""

import numpy as np
import matplotlib.pyplot as plt

N = 2**6                     # Sample size
t = np.linspace(-8, 8, N)    # N equally spaced samples on a time domain of length T = N(t[n+1]-t[n])

def h(t):
    if t >= 3 and t <= 5:
        return 4
    else:
        return 0

# =============================================================================
# Define functions and perform Fourier transform
# =============================================================================

h_signal = np.array([h(t_n) for t_n in t])
g_response = np.array([ (1/(2*np.pi)) * np.e**(- (t_n)**2 /2) for t_n in t])

# Fourier transform h(t) and g(t)
h_fft = np.fft.fft(h_signal)
g_fft = np.abs( np.fft.fft(g_response) )

# By the Convolution Theorem:
g_conv_h = np.fft.ifft( h_fft * g_fft )

# =============================================================================
# Plot results
# =============================================================================

f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,4))
ax1.plot(t, h_signal, color='red', linewidth=2)
ax1.set_xlim(0,8)
ax1.set_ylim(0,5.5)
ax1.set_title('(a)')
ax1.set_xlabel('Time')
ax1.set_ylabel('Signal function h(t)')

ax2.plot(t, g_response, color='red', linewidth=2)
ax2.set_xlim(-5,5)
ax2.set_ylim(0, 0.17)
ax2.set_title('(b)')
ax2.set_xlabel('Time')
ax2.set_ylabel('Response function g(t)')

ax3.plot(t, h_signal, label='Signal', color='silver', linewidth=2)
ax3.plot(t, g_conv_h, label='Convoluted signal', color='red', linewidth=2) 
ax3.legend(loc=1)

ax3.set_xlim(0,8)
ax3.set_ylim(0,5.5)
ax3.set_title('(c)')
ax3.set_xlabel('Time')
ax3.set_ylabel(' g convoluted with h (t)')