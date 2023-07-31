
def is_safe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_queens(board, col, solutions):
    if col >= 8:

        solutions.append([row[:] for row in board])
        return True

    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1


            solve_queens(board, col + 1, solutions)

        
            board[i][col] = 0


    return False



def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()



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
            print_board(solution) 
    else:
        print("No solutions found.")



main()
