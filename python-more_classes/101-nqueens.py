#!/usr/bin/python3
"""
101-nqueens.py
Solve the N queens problem and print all solutions.
Only sys is allowed.
"""

import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def parse_n():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def solve(n):
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    solution = [-1] * n  # solution[r] = c

    def backtrack(r):
        if r == n:
            print([[i, solution[i]] for i in range(n)])
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            solution[r] = c
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
            solution[r] = -1

    backtrack(0)


if __name__ == "__main__":
    N = parse_n()
    solve(N)

