# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:46:45 2017

@author: Shruthi
"""

import numpy as np
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    final_list = []
    xVals = np.array(x)
    yVals = np.array(y)
    for i in degs:
        model = np.polyfit(xVals , yVals, i)
        #model2 = pylab.polyfit(xVals , yVals, i)
        #print(model2)
        final_list.append(model)

    return final_list

import numpy as np
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    error = 0
    for i in range(len(y)):
        error += ((estimated[i] - y[i])**2)
    mean_error = error/len(y)
    return (1 - (mean_error/np.var(y)))
    
print(r_squared([32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0]))

