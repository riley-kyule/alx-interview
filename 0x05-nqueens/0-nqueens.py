#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

def is_safe(row, col):
    # Check if it is safe to place a queen at board[row][col]
    for i in range(row):
        if board[i][col] == 'Q' or board[i][col] == 'Q' or board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_nqueens(row):
    # Recursive function to solve the N queens problem
    if row == N:
        print_solution()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 'Q'
            solve_nqueens(row + 1)
            board[row][col] = '.'

def print_solution():
    # Print the current configuration of the board
    for i in range(N):
        row_str = ""
        for j in range(N):
            row_str += board[i][j] + " "
        print(row_str.strip())
    print()

# Create an empty board
board = [["."] * N for i in range(N)]

# Solve the N queens problem
solve_nqueens(0)

