#!/usr/bin/env python3
"""
add_matrices2D = __import__('5-across_the_planes').add_matrices2D

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
"""
def add_matrices2D(mat1, mat22):
  """Adds two matrices element-wise.

  Args:
    mat1: A list of integers and floats.
    mat2: Alist of integers and floats.

  Returns:
  A new list with the elemnt-wise sum of ar1 aand arr2.
  If mat1 and mat2 are not the same shape, returns None.
  """
  if len(mat1) != len(mat2):
    return None

  return [mat1[i] + mat2[i] for i in range(len(mat1))]