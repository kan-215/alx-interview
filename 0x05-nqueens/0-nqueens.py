#!/usr/bin/python3
""" N Queens Puzzle Solver """
import sys

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

N = int(sys.argv[1])

def place_queens(N, row=0, columns=[], diag1=[], diag2=[]):
    """Recursively generates solutions by placing queens row by row."""
    if row < N:
        for col in range(N):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                yield from place_queens(N, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])
    else:
        yield columns

def solve_nqueens(N):
    """Solve the N queens puzzle and print each solution."""
    for solution in place_queens(N):
        formatted_solution = [[row, solution[row]] for row in range(N)]
        print(formatted_solution)

solve_nqueens(N)
