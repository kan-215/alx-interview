#!/usr/bin/python3
""" Module to determine minimum operations for n H characters """

def minOperations(n):
    # If n is less than 2, no operations are possible
    if n < 2:
        return 0

    operations = 0  # Tracks the total operations performed
    divisor = 2     # Start checking divisors from 2

    while divisor <= n:
        # If the current divisor divides n evenly
        if n % divisor == 0:
            # Add the divisor to the operation count
            operations += divisor
            # Divide n by the divisor to reduce its size
            n //= divisor
        else:
            # Move to the next potential divisor
            divisor += 1

    return operations

