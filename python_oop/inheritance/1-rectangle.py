#!/usr/bin/env python3
"""Module 1-rectangle.

Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a rectangle with private width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
