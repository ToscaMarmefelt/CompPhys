#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:24:57 2018

@author: Tosca
"""

""" Interpolation using Lagrange polynomial formula """

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import itertools as it           #To enable iterating throguh two ranges at once



"""Create data set"""
# Genreate n x-values in a list
def xData(n): 
    x_list = []
    for i in range(n):
        x_list.append(10.0/n * i) 
    return x_list

#Define a simple function from which we will get our dataset
def fData(x_list):
    f_list = []
    for i in range(len(x_list)):
        f_list.append( np.cos(x_list[i] * np.pi/5.0) )    # Arbitrarily chosen non-polynomial function
    return f_list


"""Calculate the Lagrange polynomial of a given dataset"""
xi = sp.symbols('xi')

def lagrangePolynomial(x_list, f_list):
    lPolynomial = 0
    
    for i in range(len(x_list)):
        product = 1
        for j in it.chain(range(0,i), range(i+1, len(x_list))):      # For all j != i
            product = product * ( xi - x_list[j] ) / ( x_list[i] - x_list[j] )

        lPolynomial += product * f_list[i]
    
    return lPolynomial  #Returns a Lagrange polynomial as a fn of xi

#print(lagrangePolynomial(xData(n), fData(xData(n)))) 


"""Plot details"""
#Number of data points
n = 5

#Plot dataset
plt.scatter(xData(n), fData(xData(n)))
plt.title("Data set of %s points" %n)
#plt.legend('Data set')


#Plot Langrange interpolation on top of scattered data
x_interp = []
f_interp = []
for i in range(1000):
    x_interp.append(10.0/1000 * i) 
for i in range(len(x_interp)):      #Evaluate LP function for each x_interp
    f_interp.append( lagrangePolynomial(xData(n),fData(xData(n))) . subs(xi, x_interp[i]) )

plt.plot(x_interp, f_interp)
#plt.legend('Lagrange interpolation')


