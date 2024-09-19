#!/usr/bin/env python3
"""This module calculates the determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix.
  
    Args:
        matrix (list): A list whose determinant should be calculated.
   
    Returns:
        int or float: The determinant of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.

    Example:
        >>> determinant([[1, 2], [3, 4]])
        -2
  
        >>> determinant([[5]])
        5
    """

    # Ensure matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle the case for 0x0 matrix
    if matrix == [[]]:
        return 1

    # Ensure matrix is square
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for col in range(len(matrix)):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)

    return det
