#!/usr/bin/env python3


def islower(c):
  """Determina si un caracter es una letra minuscula usando codigo ASCII."""
  if ord(c) >= 97 and ord(c) <= 122:
    return True
  else:
    return False
