#!/usr/bin/python3
"""
simple Python program that solves the N queens problem using a
recursive backtracking approach to find all possible solutions:
"""

import sys


def nqueens():
    """
    N Queens
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for col in range(n)] for row in range(n)]
    solve(board, 0, n)


def solve(board, col, n):
    """
    Solve N Queens
    """
    if col == n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve(board, col + 1, n) or res
            board[i][col] = 0
    return res


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    """
    Print board
    """
    queens = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


if __name__ == "__main__":
    nqueens()