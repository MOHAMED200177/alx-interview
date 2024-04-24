#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    paste = 'H'
    text = 'H'
    operations = 0
    while (len(text) < n):
        if n % len(text) == 0:
            operations += 2
            paste = text
            text += text
        else:
            operations += 1
            text += paste
    if len(text) != n:
        return 0
    return operations
