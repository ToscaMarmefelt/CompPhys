#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:06:06 2018

@author: Tosca

1 (a) & (b) 
Write a short program to calculate the floating-point machine accuracy
of your system. 

Machine accuracy = smallest number that can be meaningfully added to AND subtracted from 1
"""

import os
import numpy as np


system = os.name

# Machine accuracy = smallest number meaningfully SUBTRACTED from 1
#def machine_accuracy_sub(precision):
#    x = precision(1/2)
#    lowest = x          
#    while (precision(1)-x) != precision(1):
#        lowest = x
#        x *= precision(1)/precision(2)
#    return lowest

# Machine accuracy = smallest number meaningfully ADDED to 1
def machine_accuracy_add(precision):
    x = precision(1/2)
    lowest = x          
    while (precision(1)+x) != precision(1):
        lowest = x
        x *= precision(1)/precision(2)
    return lowest

# =============================================================================
# Answer Question 1
# =============================================================================

answer = [["Precision", "Machine Accuracy"],
           ["", ""],
           ["Half", machine_accuracy_add(np.float16)],
           ["Single", machine_accuracy_add(np.float32)],
           ["Double", machine_accuracy_add(np.float64)]]

# Print result 
print('For Python running on a %s machine, the floating-point machine accuracy is the following: \n ' %system)
for line in answer:
    print('{:<10} {:>20}'.format(*line))
