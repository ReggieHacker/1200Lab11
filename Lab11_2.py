#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:10:34 2024

@author: reggiehacker
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

#number of flips
num_flips = 1000

#number of trials
num_trials = 1000000


#array to append number of heads to
heads_list = np.empty(num_trials)

for x in range(num_trials): 
    rng = np.random.default_rng()
    
    #create list of random numbers then convert to binary
    samples = rng.random(num_flips)
    samples2 = (samples>0.92)
    
    #find number of heads
    heads = np.sum(samples2)
 
    heads_list[x] = heads
    
#plot number of heads on a histogram
plt.hist(heads_list, bins = 500)

##running the code 1,000,000 times notes
#distribution seems similar, but a bit more precise, giving that bell curve 
#looking graph. Upon increasing the bin size to 500, I was given a beautiful
#bell curve.
            



