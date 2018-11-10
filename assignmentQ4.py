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
t = np.linspace(0, 8, N)    #

def h(t):
    if t >= 3 and t <= 5:
        return 4
    else:
        return 0

h_signal = np.array([h(t_i) for t_i in t])
g_response = np.array([ (1/(2*np.pi)) * np.e**(- (t_i - 4)**2 /2) for t_i in t])

# FOURIER TRANSFORM h(t) and g(t)

h_fft = np.fft.fft(h_signal)
g_fft = np.fft.fft(g_response)

# By the convolution theorem:

g_conv_h = np.fft.ifft( h_fft * g_fft )

plt.plot(t, h_signal, 'r')
plt.plot(t, g_response, 'b')
plt.plot(t, g_conv_h, 'g')