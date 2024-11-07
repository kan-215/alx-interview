#!/usr/bin/python3
""" 0-N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, j=0, a=[], b=[], c=[]):
    """ find possible positions """
    if j < n:
        for i in range(n):
            if i not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [j - i])
    else:
        yield a


def solve(n):
    """ solve for n """
    m = []
    j = 0
    for solution in queens(n, 0):
        for t in solution:
            m.append([j, t])
            j += 1
        print(m)
        m = []
        j = 0


solve(n)
