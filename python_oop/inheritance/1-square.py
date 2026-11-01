#!/usr/bin/env python3
"""Module 1-square.

Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a square with a private size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
