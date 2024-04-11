#!/usr/bin/python3
"""nquees task"""
import sys


def nqueens(n):
    """find the nqueens for the size of n"""
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    column = []
    diagX = []
    diagY = []

    result = []

    def backtrack(row):
        """find nqueens using backtracking"""
        if row == n:
            print(result)
            return

        for col in range(n):
            if col in column or (row + col) in diagX or (row - col) in diagY:
                continue
            column.append(col)
            diagX.append(row + col)
            diagY.append(row - col)
            result.append([row, col])

            backtrack(row + 1)

            column.remove(col)
            diagX.remove(row + col)
            diagY.remove(row - col)
            result.remove([row, col])
    backtrack(0)


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)
size = sys.argv[1]
try:
    nqueens(int(size))
except ValueError:
    print('N must be a number')
    sys.exit(1)