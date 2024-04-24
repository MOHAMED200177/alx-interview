#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    past = "H"
    text = "H"
    Operations = 0
    while (len(text) < n):
        if n % len(text) == 0:
            Operations += 2
            past = text
            text += text
        else:
            Operations += 1
            text += past
    if len(text) != n:
        return 0
    return Operations
