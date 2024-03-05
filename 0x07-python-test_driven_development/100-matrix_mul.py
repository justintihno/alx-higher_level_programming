#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list.
        TypeError: If either m_a or m_b is not a list of lists.
        ValueError: If either m_a or m_b is empty.
        TypeError: If one element of m_a or m_b is not an integer or float.
        TypeError: If m_a or m_b is not a rectangle.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list"
                      if not isinstance(m_a, list)
                      else "m_b must be a list")

    if not all(isinstance(row, list)
                for row in m_a) or not all(isinstance(row, list)
                for row in m_b):
        raise TypeError("m_a must be a list of lists"
                        if not all(isinstance(row, list) for row in m_a)
                        else "m_b must be a list of lists")

    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty"
                        if (m_a == [] or m_a == [[]])
                        else "m_b can't be empty")

    if any(not isinstance(num, (int, float))
            for row in m_a for num in row) or \
       any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats"
                        if any(not isinstance(num, (int, float))
                        for row in m_a for num in row)
                        else "m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0])
            for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size"
                        if any(len(row) != len(m_a[0]) for row in m_a)
                        else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b))
              for col_b in zip(*m_b)] for row_a in m_a]
    return result
