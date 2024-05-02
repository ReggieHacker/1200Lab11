#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:51:57 2024

@author: reggiehacker
"""

import matplotlib.pyplot as plt
import numpy as np

#define number of steps
num_step = 4000

#define number of random walks we want
num_walks = 1000

#create arrays for final coordinates of all the walks
x_final = np.empty(num_walks)
y_final = np.empty(num_walks)
displacement = np.empty(num_walks)

#for loop to make a bunch of random walks
for b in range(num_walks):
    #generate random array
    rng = np.random.default_rng()
    
    #Define two seperates lists, one for each direction
    y = rng.random(num_step) > 0.5
    x = rng.random(num_step) > 0.5
    
    #Make them negative 1 or positive 1
    y = 2*y - 1
    x = 2*x - 1
    
    #add lists together to find final coords
    x = np.cumsum(x)
    y = np.cumsum(y)
    
    #append final values to the previous made arrays
    x_final[b - 1] = x[num_step - 1]
    y_final[b - 1] = y[num_step - 1]
    displacement[b - 1] = np.sqrt((x[num_step - 1])**2 + (y[num_step - 1])**2)
    
    
#square displacement
displacement_sqrd = displacement * displacement

#find average displacement
avg_dis = np.mean(displacement_sqrd)

#create histogram of data
plt.hist(displacement_sqrd, bins=50)

#print results
print("The average displacement of a 1000 random walks is ", avg_dis)




    

