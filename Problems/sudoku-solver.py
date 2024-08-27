class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(board, row, col, num):
            # Check if the number is not repeated in the current row, column, and sub-grid
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                # Check the 3x3 sub-box
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # Try placing digits 1-9 in the empty cell
                        for num in map(str, range(1, 10)):
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if solve(board):  # Recursively solve the rest of the board
                                    return True
                                board[row][col] = '.'  # Backtrack if not solvable
                        return False  # If no number can be placed, return False
            return True  

        solve(board)
