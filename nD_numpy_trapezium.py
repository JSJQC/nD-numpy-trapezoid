# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:11:03 2021

@author: jakes
"""

import numpy as np

m, k, T = (1.67493E-27, 1.38064852E-23, 1E5)

## Define functions here ------------------------------------------------------

def square(x):
    
    return x ** 2

def triple_square(xlist):
    
    return square(xlist[0]) + square(xlist[1]) + square(xlist[2])

def Maxwellian(x):
    
    return (np.pi * 4) * (m / (np.pi * 2 * k * T)) ** (3 / 2) * (x ** 2) * np.exp((- m * x ** 2) / (2 * k * T))

def double_maxwellian(xlist):
    
    return Maxwellian(xlist[0]) * Maxwellian(xlist[1])

def triple_maxwellian(xlist):
    
    return Maxwellian(xlist[0]) * Maxwellian(xlist[1]) * Maxwellian(xlist[2])

## ----------------------------------------------------------------------------

## n-D solutions --------------------------------------------------------------

def create_ordered_sets(x, dims): # x is a list of length n
    
    print ()
    print ("Creating the coordinate system, this may take a little while...")
    
    return np.array(np.meshgrid(*x)).T.reshape(-1, dims)

def get_axes(ordered_sets, dims): # ordered_sets should be as the object produced above

    print ()
    print ("Rearranging into axes, bear with me...")
    axes = []
    for column in range(dims):
        x = ordered_sets[:,column]
        axes.append(x)
    
    return axes
    

def nD_trapzf(func, a, b, n, dims): # a, b, n are lists of length n

    x = [np.linspace(a[i], b[i], n[i]) for i in range(len(a))]
    
    ordered = create_ordered_sets(x, dims)
    x = get_axes(ordered, dims)
    
    y = func(x)

    
    hs = []
    
    for i in range(len(n)):
        h = (b[i] - a[i]) / (n[i] - 1)
        hs.append(h)
    hs = np.array(hs)
    
    print ()
    print ("h-values calculated, working on evaluating the sums")
    
    return ( (hs.prod()) / 2) * (y[1:] + y[:-1]).sum()
    
    

if __name__ == "__main__":
    
    a = [0, 0]
    b = [80000, 80000]
    n = [15000, 15000]
    dims = 3

    #approx_square = nD_trapzf(triple_square, a, b, n, 3)
    approx_2dmaxwell = nD_trapzf(double_maxwellian, a, b, n, 2)
    #approx_3dmaxwell = nD_trapzf(triple_maxwellian, a, b, n, 3)
    '''
    print ()
    print ("Approximate triple square value:")
    print (approx_square)
    print ()
    print ("Approximate triple maxwellian value:")
    print (approx_3dmaxwell)
    '''
    
    print ()
    print ("Approximate double maxwellian value:")
    print (approx_2dmaxwell)
    