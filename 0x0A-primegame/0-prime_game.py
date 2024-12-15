#!/usr/bin/python3
"""Determines the winner of a prime game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_win = 0
    maria_win = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for j in range(2, len(a)):
        rm_multiples(a, j)

    for j in nums:
        if sum(a[0:j + 1]) % 2 == 0:
            ben_win += 1
        else:
            maria_win += 1
    if ben_win > maria_win:
        return "Ben"
    if maria_win > ben_win:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for j in range(2, len(ls)):
        try:
            ls[j * x] = 0
        except (ValueError, IndexError):
            break
