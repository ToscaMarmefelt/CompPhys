#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:26:27 2018

@author: Tosca
"""

import random
import numpy as np

# Decide on number of columns and rows for test matrices A and B
col_a = random.randint(1,10)           #Range 1-10 for simplicity
row_a = random.randint(1,10)          

col_b = row_a
row_b = col_a                       # To ensure matrix multiplication is possible

# Generate random matrices
entries = col_a * row_a 

a = []
b = []

for i in range(entries):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
    
a = np.reshape(a, (col_a, row_a))
b = np.reshape(b, (col_b, row_b))




# Function for performing matrix multiplication of any two matrices m1 and m2
def matrixMultiplication(m1, m2):
    
    # Check that matrices can be multiplied
    if len(m1) != len(m2[0]) or len(m1[0]) != len(m2):
        print("Sorry, you cannot perform matrix multiplication on these matrices.")
    
    # Multiply matrices m1 and m2 to give resulting matrix c
    c = []
    for i in range(len(m1)):            #For every row in m1
        
        for j in range(len(m2[0])):     #For every column in m2
            c_entry = np.sum ( np.array(m1[i]) * np.array(m2[:,j]) )
            c.append(c_entry)
    
    c = np.reshape(c, (len(m1[0]),len(m1)))
    
    return c




""" Run calculation """

c = matrixMultiplication(a,b)

print("A = ", a, ",B = ", b, " and C = ", c) 
#Comparing to np.dot(a,b), it gives the same! 
    
    
    