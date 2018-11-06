#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:37:00 2018

@author: Tosca

Carry out LU decomposition of an arbitrary NxN matrix using Crout's method.
"""
import numpy as np 


""" Use Crout's method for decomposing a square matrix A into
    an upper and a lower matrix.
"""

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

# Calculate the determinant of a square (already decomposed) matrix A=L*U
def detLU(matrix):      
    
    product = 1
    for n in range(len(matrix)):
        product *= matrix[n][n]
    
    return product


""" Answer question 2
"""

matrixA = np.array([[3., 1., 0., 0., 0.],
                   [3., 9., 4., 0., 0.],
                   [0., 9., 20., 10., 0.],
                   [0., 0., -22., 31., -25.],
                   [0., 0., 0., -55., 60.]])
 
print('L*U = \n', decompose(matrixA))
#print('matrixA = ', matrixA)
print('det(A) = ', detLU(matrixA))
