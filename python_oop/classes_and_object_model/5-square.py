#!/usr/bin/env python3
"""Module 5-square.

Defines a Square class with validation, area, and printing capabilities.
"""


class Square:
    """Represents a square with private size and print method."""

    def __init__(self, size=0):
        """Initializes the square with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' character in stdout."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
