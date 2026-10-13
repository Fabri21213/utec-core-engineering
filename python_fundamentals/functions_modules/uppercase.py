#!/usr/bin/env python3


def uppercase(str_arg):
    """Imprime una cadena en mayusculas utilizando conversion ASCII (ord y chr)."""
    new_str = ""
    for c in str_arg:
        # Si el caracter esta entre 'a' (97) y 'z' (122)
        if ord(c) >= 97 and ord(c) <= 122:
            # Le restamos 32 para convertirlo a mayuscula
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print(new_str)
