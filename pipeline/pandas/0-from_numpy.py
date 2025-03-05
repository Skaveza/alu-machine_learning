#!/usr/bin/env python3
import numpy as np
import pandas as pd

"""This module creates a pd.DataFrame from a np.ndarray"""

def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray"""
    
    # Define index and column names
    index_values = ['0', '1', '2', '3', '4', '5', '6']
    column_values = ['A', 'B', 'C']

    # Create DataFrame
    df = pd.DataFrame(data=array, index=index_values, columns=column_values)
    return df

# Creating a numpy array
array = np.array([[-1, 4, 7], [2, 4, 8], [3, 9, 27],  
                  [4, 16, 64], [5, 25, 125], [6, 36, 216],  
                  [7, 49, 343]]) 

# Call the function
df = from_numpy(array)
print(df)
