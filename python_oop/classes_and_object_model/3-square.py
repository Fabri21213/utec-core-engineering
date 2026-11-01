#!/usr/bin/env python3
"""Definición de una clase Square con validación y cálculo de área."""


class Square:
    """Una clase Square que representa un cuadrado con método para calcular el área."""

    def __init__(self, size=0):
        """Inicializa un cuadrado validando el tipo y valor de size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcula y devuelve el área actual del cuadrado."""
        return self.__size ** 2
