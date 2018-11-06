#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:37:00 2018

@author: Tosca

Carry out LU decomposition of an arbitrary NxN matrix using Crout's method.
"""
import numpy as np 
import random


""" Use Crout's method for decomposing a square matrix A into
    an upper and a lower matrix.
"""
#def decomposeNew(A):
#    luMatrix = np.empty( (len(A),len(A)), int)
#    
#    for j in range(len(A)):
#        #luMatrix[0][j] = A[0][j]    # Beta[1][j] is just A[0][j] bc no sum
#        
#        for i in range(j):           # Calculate all Beta values for given j
#            mySumB = 0
#            for k in range(i-1):
#                mySumB += luMatrix[i][k] * luMatrix[k][j]
#            luMatrix[i][j] = ( A[i][j] - mySumB )
#            
#        for i in range((j+1),len(A)):  # Calculate all Alpha values for given j
#            mySumA = 0
#            for k in range(j-1):
#                mySumA += luMatrix[i][k] * luMatrix[k][j]
#            luMatrix[i][j] = ( 1/luMatrix[j][j] * (A[i][j] -mySumA ))  
#    return luMatrix


#Alternative method where we just place new values in original matrix
def decompose(myMatrix):
    
    for j in range(len(myMatrix)):   # For each column j
        
        #BETA
        for i in range(j+1):
#            print( 'beta (i,j)=(', i,',', j, ')')
            mySumB = 0
            for k in range(i):
#                print('b: i=', i,'j=', j, 'k=', k)
                mySumB += myMatrix[i][k] * myMatrix[k][j]
            myMatrix[i][j] = ( myMatrix[i][j] - mySumB )
#            print('mySumB=', mySumB)
#            print('New entry: ', myMatrix[i][j], '\n')

         
        #ALPHA
        for i in range((j+1),len(myMatrix)):
#            print('alpha (i,j)=(', i,',', j, ')')
            mySumA = 0
            for k in range(j):
#                print('a: i=', i,'j=', j, 'k=', k)
                mySumA += myMatrix[i][k] * myMatrix[k][j]
#            print('myMatrix[j][j]=', myMatrix[j][j], 'myMatrix[i][j]=', myMatrix[i][j])
            myMatrix[i][j] = ( 1/myMatrix[j][j] * myMatrix[i][j] -mySumA )
#            print('mySumA=', mySumA)
#            print('New entry: ', myMatrix[i][j], '\n')

    
    return myMatrix

# Calculate the determinant of a square matrix A
def detA(myMatrix):
#    decompose(myMatrix)
    
    product = 1
    for n in range(len(myMatrix)):
        product *= myMatrix[n][n]
    
    return product


""" Generate a random NxN matrix
    Returns an array of N lists, each with N entries.
"""
#myMatrix = []
#N = 3                       # random.randint(0,10) if we do not wish to set N
#
#for i in range(N**2):
#    myMatrix.append(random.randint(0,10))
#myMatrix = np.reshape(myMatrix, (N,N))

""" Test code
"""
matrixA = np.array([[3., 1., 0., 0., 0.],
                   [3., 9., 4., 0., 0.],
                   [0., 9., 20., 10., 0.],
                   [0., 0., -22., 31., -25.],
                   [0., 0., 0., -55., 60.]])
 
#print('A = ', matrixA)
print('L*U = \n', decompose(matrixA))
#lu = decompose(matrixA)
#print(lu) 
#print('det A = ', detA(matrixA)) 
