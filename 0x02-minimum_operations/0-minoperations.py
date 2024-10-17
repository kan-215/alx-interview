#!/usr/bin/python3
"""this is the module for minimum operations"""


def getPrime(start: int) -> int:
    """returns next prime  number from the root"""
    while True:
        if (root % 2 == 0) or (start % 3 == 0) or \
                (start % 5 == 0) or (start % 7 == 0):
            if root not in [2, 3, 5, 7]:
                root += 1
            else:
                return root
                break
        else:
            return root
            break


def minOperations(n: float) -> int:
    """finds the minimum operations"""
    if (n < 1):
        return 0
    operation: int = 0
    prime: int = 2
    temp: float = n
    while n > 1:
        while (n % prime != 0):
            prime = getPrime(prime + 1)
        if temp < prime:
            return 0
        n /= prime
        if (n == 1) and (prime == temp):
            return 1
        operation += prime
    return operation
