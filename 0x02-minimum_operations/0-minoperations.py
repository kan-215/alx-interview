#!/usr/bin/python3
"""0-minoperations module"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 characters
    if (n < 2):
        return 0
    operations, divisor = 0, 2
    while divisor <= n:
        # if n is evenly divided by the divisor
        if n % divisor == 0:
            # total even-divisions by divisor equals total operations
            operations += divisor
            # set n to the remainder
            n = n / divisor
            # reduce root to find remaining smaller values that evenly-divide n
            divisor -= 1
        # increment root until it evenly-divides n
        divisor += 1
    return operations
