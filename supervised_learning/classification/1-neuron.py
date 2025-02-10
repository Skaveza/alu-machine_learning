#!/usr/bin/env python3

import numpy as np


"""This module defines a single neuron performing binary classification"""

class Neuron: """Defines the single neuron"""

def __init__(self,nx):
  """nx represents the number of input features to a neuron"""
  
  if isinstance(nx,int): raise TypeError
  """nx must be an integer"""

if nx < 1: raise ValueError 
"""nx must be positive"""

#Private attributes
"""Initializing private instance attributes, each private attribute has a corresponding getter function"""
self .__W = np.random.randn(1,nx)
self .__b = 0
self .__A = 0 

#Getters
"""These are the getters for the private attributes"""
def W(self):
        return self.__W
      
def b(self):
        return self.__b
      
def A(self):
        return self.__A
