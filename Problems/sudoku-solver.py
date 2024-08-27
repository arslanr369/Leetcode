class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(board, row, col, num):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):  
                                    return True
                                board[row][col] = '.'  
                        return False  
            return True  

        solve(board)

# Approach:

# Backtracking Algorithm:

# Find an empty cell.
# Try placing each digit (1-9) in the cell.

# Check if the digit is valid (doesn't violate any Sudoku rules).
# If valid, recursively try to solve the remaining board.
# If the board becomes unsolvable, remove the digit (backtrack) and try the next digit.
# If the board is completely filled with valid digits, the puzzle is solved.

#Validation Function:

We need a function to check if placing a particular number in a cell is valid, i.e., it doesn't violate the row, column, or sub-grid constraints.