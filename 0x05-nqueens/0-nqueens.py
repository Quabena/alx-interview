#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[], solutions=[]):
    """Recursive backtracking solution to the N Queens problem."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board.append(col)
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def main():
    """Main entry point of the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
