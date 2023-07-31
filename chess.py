# Function to check if a queen can be placed at the given position
def is_safe(board, row, col):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # If all checks pass, the position is safe
    return True


# Function to solve the 8-queen problem using backtracking
def solve_queens(board, col, solutions):
    if col >= 8:
        # All queens have been placed successfully
        solutions.append([row[:] for row in board])  # Store the solution
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place the remaining queens
            solve_queens(board, col + 1, solutions)

            # Backtrack and try the next row
            board[i][col] = 0

    # If no solution found, return False
    return False


# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()


# Main function to solve and display the 8-queen problem
def main():
    # Initialize the chessboard
    board = [[0 for _ in range(8)] for _ in range(8)]
    solutions = []

    solve_queens(board, 0, solutions)

    if solutions:
        print("Total solutions found:", len(solutions))
        print()
        for i, solution in enumerate(solutions):
            print("Solution", i + 1)
            print_board(solution)  # Print the board from the solution list
    else:
        print("No solutions found.")


# Run the main function
main()
