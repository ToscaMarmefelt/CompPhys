#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:32:44 2018

@author: Tosca
"""

import astropy.stats as ap
import matplotlib.pyplot as plt


t = []          # unit: 10**(-12) s
sigma = []      # unit: 10**(-12) s

file = open("lifetime.txt", "r")
for line in file:
    t.append(float(line.split(' ')[0]))
    sigma.append(float(line.split(' ')[1]))

# =============================================================================
# Plot histograms of data in lifetime.txt
# =============================================================================

bins_t = ap.histogram(t, bins='freedman')[1]
bins_sigma = ap.histogram(sigma, bins='freedman')[1]

f, (ax1, ax2) = plt.subplots(1,2, figsize=(15,6), sharey=True)

ax1.hist(t, bins=bins_t, color='red')
ax1.set_title('(a)')
ax1.set_xlabel('Decay time (ps)')
ax1.set_ylabel('Number of occurances')
#ax1.legend(loc=1)

ax2.hist(sigma, bins=bins_sigma, color='red')
ax2.set_title('(b)')
ax2.set_xlabel('Uncertainty in measurement (ps)')
ax2.legend(loc=1)