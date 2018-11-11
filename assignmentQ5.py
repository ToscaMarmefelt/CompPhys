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

#ap.hist(x, bins='freedman')


# =============================================================================
# Transformation method
# =============================================================================
yTrans = [np.arccos( 1-2*xn ) for xn in x]
#ap.hist(yTrans, bins='freedman') 


# =============================================================================
# Rejection method
# =============================================================================



#def reject(yList):
#    #Collect all y-values which are accepted by the rejection method
#    yReject = []
#    
#    for yi in yList:
#        
#        #Choose p_i by applying transformation method to f(y)=2/np.pi * np.sin(y) 
#        p_i = np.arccos( 1 - 2*yi )
#        if yi < p_i:
#            yReject.append(yi)
##    print('yReject = ', yReject)
#    return yReject


# Define desired probability distribution function
def P(y):
    return (2/np.pi)*(np.sin(y))**2


def reject(samplesWanted):
    #Collect all y-values which are accepted by the rejection method into a list
    yReject = []
    
    while len(yReject) < samplesWanted:
        yi = np.arccos(1 - 2*random.random())
        #Choose p_i by applying transformation method to f(y)=2/np.pi * np.sin(y)
        p_i = np.arccos(1 - 2*yi) * random.random()
        
        if P(yi) >= p_i:
            yReject.append(yi)
    return yReject


N = 10**5
ap.hist(reject(N), bins='freedman')