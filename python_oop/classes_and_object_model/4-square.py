#!/usr/bin/env python3
"""Module 4-square.

Defines a Square class with property getters and setters.
"""


class Square:
    """Represents a square with private size and validation."""

    def __init__(self, size=0):
        """Initializes the square with size validation."""
        self.size = size

    @property
    def size(s):
        """Retrieves the current size of the square."""
        return s.__size

    @size.setter
    def size(s, value):
        """Sets the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        s.__size = value

    def area(s):
        """Returns the current square area."""
        return s.__size ** 2
