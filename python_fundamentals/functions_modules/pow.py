#!/usr/bin/env python3


def pow(a, b):
    """Calcula a elevado a la potencia b usando un bucle, sin usar **."""
    if b == 0:
        return 1

    result = 1
    # Si b es positivo
    if b > 0:
        for _ in range(b):
            result *= a
    # Si b es negativo
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result

    return result
