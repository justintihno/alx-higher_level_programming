#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both m_a and m_b must be lists of lists")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) or \
       any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("All elements of m_a and m_b must be integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("All rows of m_a and m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("The number of columns in m_a must equal the number of rows in m_b")

    if not m_a or not m_b:
        raise ValueError("Both m_a and m_b must be non-empty")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
