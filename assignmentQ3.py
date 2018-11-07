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

from assignmentQ2 import decompose, makeL, makeU, solveEquation

#From lists of data points xList and yList, generate one row of matrix for each i (from 1 to n-1)

def cubicSpline(xList, yList):
    """
    Implement Equation 4.15 to generate a matrix equation. Solve this using the routine
    from Q2 to generate functions on the intervals. 
    
    xList:      List of original data points in x
    yList:      List of original data points in y
    """
    matrix = []
    bVector = []
    
    #CREATE MATRIX AND VECTOR
    for i in range(1, len(xList)-1):
#        print('i = ', i)
        a_i = [0] * (len(xList))  
#        print('1: a_i = ', a_i)
        a_i[i-1], a_i[i], a_i[i+1] = (xList[i]-xList[i-1])/6, (xList[i+1]-xList[i-1])/3, (xList[i+1]-xList[i])/6
#        print('2: a_i = ', a_i)
        b_i = ( (yList[i+1]-yList[i]) / (xList[i+1]-xList[i-1]) ) - ( (yList[i]-yList[i-1]) / (xList[i]-xList[i-1]) )
#        print('1: b_i = ', b_i)
        
        matrix.append(a_i[1:-1])
        bVector.append(b_i)
    
#    bVector = bVector[1:-1] 
#    print('matrix = ', matrix)
    
    #SOLVE MATRIX EQUATION FOR SECOND DERIVATIVE F
    lu = decompose(matrix)
    f2Vector = solveEquation( makeL(lu), makeU(lu), bVector )
    
    return f2Vector 



# =============================================================================
# Perform linear interpolation on set of data 
# =============================================================================

xTest = [1., 2., 4., 7., 8., 11.]
yTest = [10., 5., 3., 9., 3., 5.]
#plt.scatter(xTest, yTest)

print( cubicSpline(xTest, yTest) )

#xRange =  np.linspace(1.,8.,100) #10 data points in the range 0-10 (including 10)
#interFuncs = linearFunction(xTest, yTest)
#xValues = linearInterpolation(xTest, xRange, interFuncs)[0]
#yValues = linearInterpolation(xTest, xRange, interFuncs)[1]

#print('fList = ', interFuncs)
#print('xValues = ', xValues)
#print('yValues = ', yValues)

#plt.plot(xValues, yValues, 'r')
#plt.show()

        
        