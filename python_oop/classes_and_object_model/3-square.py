#!/usr/bin/env python3
"""Module 3-square.

Defines a Square class with validation and area.
"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with size validation."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
