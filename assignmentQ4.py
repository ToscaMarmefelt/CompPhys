#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:57:52 2018

@author: Tosca

Question 4: Fourier Transforms

"""

import numpy as np
#from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

N = 2**6                    #Sample size
t = np.linspace(-8, 8, N)    #N equally spaced samples on a time domain of length T = N(t[n+1]-t[n])

def h(t):
    if t >= 3 and t <= 5:
        return 4
    else:
        return 0

h_signal = np.array([h(t_n) for t_n in t])
g_response = np.array([ (1/(2*np.pi)) * np.e**(- (t_n-4)**2 /2) for t_n in t])

# FOURIER TRANSFORM h(t) and g(t)

h_fft = np.fft.fft(h_signal)
#g_fft = np.fft.fftshift ( np.fft.fft(g_response) )
g_fft = np.abs( np.fft.fft(g_response) )

# By the Convolution Theorem:

g_conv_h = np.fft.ifft( h_fft * g_fft )

plt.plot(t, h_signal, 'r')
plt.plot(t, g_response, 'b')
plt.plot(t, g_conv_h, 'g')

