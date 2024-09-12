#!/usr/bin/env python3
"""
matrix_shape = __import__('2-size_me_please').matrix_shape

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
"""

def matrix_shape(matrix):
  """ Calculates the shape of a matrix
  
  Args:
     matrix: The matrix to calculate the shape of.
     
  Returns:
     A tuple containing the number of rows and columns in the matrix.
    """
  
  num_rows = len(matrix)
  num_cols = len(matrix[0])
  
  return num_rows, num_cols