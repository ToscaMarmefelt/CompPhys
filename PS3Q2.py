#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:39:59 2018

@author: Tosca
"""

import random
import numpy as np

# Generate random 3x3 matrix and 3-vector

myMatrix = []
for i in range(9):
    myMatrix.append(random.randint(0,10))
myMatrix = np.reshape(myMatrix, (3,3))

myVector = []
for i in range(3):
    myVector.append(random.randint(0,10))

print("myVector = ", myVector, " and myMatrix = ", myMatrix)



# Define a function that returns a 3-vector x which satisfies Ax=b

def gaussianElimination(A,b):
    
    # Check that there are no zeros in the diagonal of the matrix
    
    
    # Perform Gaussian elimination
    for j in range(len(A[0])):                  # For every column
        b[j] = b[j]/A[j][0]
        A[j] = np.array(A[j]/A[j][0])
        
        for i in range(len(A)):                 # For every row
            A[j][i], 
            
        
            
            
            
            
            
            