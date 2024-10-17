#!/usr/bin/python3
""" 0-minoperations module"""


def minOperations(n):
    """
    minOperations
    gets the min number of operations required to generate exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operations =0
    divisor = 2
    while divisor <= n:
        # if n evenly divides by root
        if n % divisor == 0:
            # total even-divisions by root = total operations
            operations += divisor
            # set n to the remainder
            n = n / divisor
            # reduce root to find remaining smaller vals that evenly-divide n
            divisor -= 1
        # increment root until it evenly-divides n
        divisor += 1
    return operations
