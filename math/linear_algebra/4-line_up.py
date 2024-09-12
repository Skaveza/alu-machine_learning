#!/usr/bin/env python3
"""
add_arrays = __import__('4-line_up').add_arrays

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))
"""

def matrix_transpose(matrix):
    """Transposes a matrix.
  
    Args:
        matrix: A 2D list (matrix) to transpose.
  
    Returns:
        A new transposed matrix where the rows and columns are swapped.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
