#!/usr/bin/env python3
"""Module base_geometry.

Defines a BaseGeometry class.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as an integer greater than 0."""
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
