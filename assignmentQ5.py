#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:02:05 2018

@author: Tosca

Question 5: Random numbers
"""

import random
import numpy as np
import astropy.visualization as ap
import matplotlib.pyplot as plt


# =============================================================================
# Uniform probability distribution
# =============================================================================
x = []
for i in range(10**5):
    x.append(random.random())

ap.hist(x, bins='freedman')


# =============================================================================
# Transformation method
# =============================================================================
yTrans = [np.arccos( 1-2*xn ) for xn in x]
ap.hist(yTrans, bins='freedman') 


# =============================================================================
# Rejection method
# =============================================================================


