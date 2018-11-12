#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:37:00 2018

@author: Tosca

Carry out LU decomposition of an arbitrary NxN matrix using Crout's method.
"""
import numpy as np 


# =============================================================================
# Use Crout's method to decompose a square matrix into an upper and a lower matrix
# =============================================================================

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



# =============================================================================
# Solve matrix equation LUx = b for vectors x, b
# =============================================================================

def solveEquation(L, U, b):
    
    #Forward substitution to solve for y (from Ly=b)
    y = []
    y.append( b[0] / L[0][0] )
    
    for i in range(1,len(b)):               # i=1, 2, 3, 4 for our b
        sumY = 0
        for j in range(i-1):
            sumY += L[i][j] * y[j]
        y.append( 1./L[i][i] * (b[i] - sumY) )
#    print('y =', y)
        
    #Backward substitution to solve for x (from Ux=y)
    x = []
    x.insert(0, (y[len(b)-1] / U[len(b)-1][len(b)-1] ))
    
    for i in range( (len(b)-2), -1, -1 ):   # i=3, 2, 1, 0 for our b
        sumX = 0
        for j in range(i,len(b)):
#            print('x = ', x)
#            print('(i, j) = (', i, ',',j, ')')
#            print('U[i][j]=', U[i][j], 'and x[j]=', x[j]) 
            sumX += U[i][j] * x[j-len(b)+1]
        x.insert(0, ( 1./U[i][i] * (y[i] - sumX) ))
    
    # Return list of 
    return x
        

# =============================================================================
# Answer Question 2
# =============================================================================

matrixA = np.array([[3., 1., 0., 0., 0.],
                   [3., 9., 4., 0., 0.],
                   [0., 9., 20., 10., 0.],
                   [0., 0., -22., 31., -25.],
                   [0., 0., 0., -55., 60.]])

lu = decompose(matrixA)
determinant = detLU(lu)
print('L*U = \n', lu)
print('det(A) = ', determinant)


#LOWER
def makeL(lu):
    matrixL = np.identity(len(lu))
    for i in range(len(lu)):
        matrixL[i][0:i] = lu[i][0:i]        #Keep 1s on diagonal 
    return matrixL

#UPPER
def makeU(lu):
    matrixU = np.identity(len(lu))
    for i in range(len(lu)):
        matrixU[i][i:] = lu[i][i:]
    return matrixU

#print('matrixL = \n', matrixL)
#print('matrixU = \n', matrixU) 

bVector = np.array([2., 5., -4., 8., 9.])
matrixL = makeL(lu)
matrixU = makeU(lu)
xVector = solveEquation( matrixL, matrixU, bVector )

#print('x = \n', xVector)
#x = [-0.26810222024018593, 
#       1.0999144334855182, 
#       -0.49543663973599689, 
#       0.041044412500957146, 
#       0.30430795221431156]


""" Use routines above to calculate the inverse of A
"""
inverseA = [[], 
            [], 
            [], 
            [], 
            [] ]

for j in range(len(matrixA)):       # For every column
    # Pick out relevant column of identity matrix
    b_j = [0] * len(lu)
    b_j[j] = 1
    
    # Solve matrix equation LU*x_j = b_j
    x_j = solveEquation(matrixL,matrixU, b_j)
    for i in range(len(matrixA)):   # For every row
        inverseA[i].append(x_j[i]) 

print('inverseA = ', inverseA)
        
