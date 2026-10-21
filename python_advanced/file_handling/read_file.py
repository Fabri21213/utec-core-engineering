#!/usr/bin/env python3
"""
Module to read a text file and print it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
