#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:49:07 2018

@author: Tosca

Question 3: Interpolation
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Linear interpolation
# =============================================================================

def linearFunction(xList, yList):
#   Define a linear function {f_i(x) = k_i*x + m_i} between every set of points i and i+1
    
    f_i = []
    for i in range(len(xList)-1):
        k_i =  (yList[i+1]-yList[i]) / (xList[i+1]-xList[i])
        m_i = yList[i] - k_i * xList[i] 
        f_i.append([k_i, m_i])
        
    return f_i
    

def linearInterpolation(xList, xRange, fList):
    """ 
    To plot interpolation function for entire range of x (every value in xRange),
    we must determine what function i to call for each value
    
    xList:      List of original data points in x
    xRange:     List of x for which we want to plot the interpolated function
    fList:      List of functions over each defined interval 
    """ 
    interpX = []
    interpY = []
    n = 0
    
    for i in range(1,len(xList)):
#        print('i = ', i)
#        for n in range(len(xRange)-1):
#            print('n = ', n)
#            print( 'xRange[n] = ', xRange[n], ' and xList[i] = ', xList[i])
        
        while xRange[n] <= xList[i]:
#            print('n = ', n)
#            print( 'xRange[n] = ', xRange[n], ' and xList[i] = ', xList[i])
            interpX.append( xRange[n] )
            interpY.append( fList[i-1][0]*xRange[n] + fList[i-1][1] )
#            print('interpY = ', interpY)
            n += 1
    
    return interpX, interpY


# =============================================================================
# Cubic spline interpolation
# =============================================================================

#from assignmentQ2 import decompose, solveEquation




# =============================================================================
# Perform linear interpolation on set of data 
# =============================================================================

xTest = [1., 2., 4., 7.]
yTest = [10., 5., 3., 9.]
plt.scatter(xTest, yTest)


xRange =  np.linspace(1.,8.,100) #10 data points in the range 0-10 (including 10)
interFuncs = linearFunction(xTest, yTest)
xValues = linearInterpolation(xTest, xRange, interFuncs)[0]
yValues = linearInterpolation(xTest, xRange, interFuncs)[1]

#print('fList = ', interFuncs)
#print('xValues = ', xValues)
#print('yValues = ', yValues)

plt.plot(xValues, yValues)
plt.show()

        
        