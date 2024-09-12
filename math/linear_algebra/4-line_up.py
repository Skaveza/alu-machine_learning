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

def add_arrays(arr1, arr2):
  """Adds two arrays element-wise.

  Args:
    arr1: A list of integers and floats.
    arr2: Alist of integers and floats.
  
  Returns:
  A new list with the elemnt-wise sum of ar1 aand arr2.
  If arr1 and arr2 are not the same shape, returns None.
  """
  if len(arr1) != len(arr2):
    return None

  return [arr1[i] + arr2[i] for i in range(len(arr1))]
