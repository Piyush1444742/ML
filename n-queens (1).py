
# N-Queens Problem using Backtracking

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    # All queens are placed
    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main Program
n = int(input("Enter the value of N: "))

board = [[0 for j in range(n)] for i in range(n)]

if solve(board, 0, n):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")
