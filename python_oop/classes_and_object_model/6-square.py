#!/usr/bin/env python3
"""Module 6-square.

Defines a Square class with size, position, validation, area, and printing.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation."""
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' and position in stdout."""
        print(self, end="")

    def __str__(self):
        """Returns the string representation of the square."""
        if self.__size == 0:
            return ""

        s = ""
        for _ in range(self.__position[1]):
            s += "\n"
        for i in range(self.__size):
            s += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                s += "\n"
        return s
