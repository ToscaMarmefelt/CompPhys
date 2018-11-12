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
    Input parameters:
        
    xList:      List of original data points in x
    xRange:     List of x for which we want to plot the interpolated function
    fList:      List of functions over each defined interval 
    """ 
    interpX = []    # List to collect x-values for interpolated function
    interpY = []    # List to collect y-values of interpolated function
    n = 0
    
    for i in range(1,len(xList)):
        
        while (n <= len(xRange)-1) and xRange[n] <= xList[i]:
#            print('i = ', i)
#            print('n = ',n)
            # Append used x-values to ensure equal length of returned x- and y-lists
            interpX.append( xRange[n] ) 
            # Calculate the value of the interpolated function at given x
            interpY.append( fList[i-1][0]*xRange[n] + fList[i-1][1] )   
            
            # Loop through entire set of xRange
            n += 1
            
    return interpX, interpY


# =============================================================================
# Cubic spline interpolation
# =============================================================================

from assignmentQ2 import decompose, makeL, makeU, solveEquation

#From lists of data points xList and yList, generate one row of matrix for each i (from 1 to n-1)

def cubicSpline(xList, yList, xRange):
    """
    Implement Equation 4.15 to generate a matrix equation. Solve this using the routine
    from Q2 to generate functions on the intervals. 
    
    xList:      List of original data points in x
    yList:      List of original data points in y
    xRange:     List of x for which we want to plot the interpolated function
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
    f2Vector = [0] + f2Vector + [0]
    
    # Append 0 as first and last emtry of f2Vector list
    
    interpX = []
    interpY = []
    n = 0
    
    for i in range(1, len(xList)-1): #len-1
        
        while n < len(xRange) and xRange[n] <= xList[i]:
            interpX.append(xRange[n])
            
            Ai = (xList[i+1] - xRange[n]) / (xList[i+1] - xList[i]) 
            Bi = 1- Ai
            Ci = (xList[i+1]-xList[i])**2 / 6 * (Ai**3 - Ai)
            Di = (xList[i+1]-xList[i])**2 / 6 * (Bi**3 - Bi)
            
            interpY.append(Ai*yList[i] + Bi*yList[i+1] + Ci*f2Vector[i] + Di*f2Vector[i+1])
    
    return interpX, interpY 


# =============================================================================
# Test functions
# =============================================================================

#xTest = [1., 2., 4., 7., 8., 11.]
#yTest = [10., 5., 3., 9., 3., 5.]
#plt.scatter(xTest, yTest)

#print( cubicSpline(xTest, yTest) )

#xRange =  np.linspace(1.,8.,100) #10 data points in the range 0-10 (including 10)
#interFuncs = linearFunction(xTest, yTest)
#xValues = linearInterpolation(xTest, xRange, interFuncs)[0]
#yValues = linearInterpolation(xTest, xRange, interFuncs)[1]

#print('fList = ', interFuncs)
#print('xValues = ', xValues)
#print('yValues = ', yValues)

#plt.plot(xValues, yValues, 'r')
#plt.show()

# =============================================================================
# Answer Question 3
# =============================================================================

x = [-2.1, -1.45, -1.3, -0.2, 0.1, 0.15, 0.8, 1.1, 1.5, 2.8, 3.8]
y = [0.012155, 0.122151, 0.184520, 0.960789, 0.990050, 0.977751, 0.527292, 0.298197, 0.105399, 3.936690*10**-4, 5.355348*10**-4]

xRange =  np.linspace(-2.1, 3.8, 50)


xLin = linearInterpolation(x, xRange, linearFunction(x, y))[0]
yLin = linearInterpolation(x, xRange, linearFunction(x,y))[1]

xCub = cubicSpline(x, y, xRange)[0]
yCub = cubicSpline(x, y, xRange)[1]


plt.plot(xLin, yLin, 'r')
plt.plot(xCub, yCub, 'b')
