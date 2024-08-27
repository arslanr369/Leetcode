class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                num = board[i][j]
                
                box_index = (i // 3) * 3 + (j // 3)
                
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        return True

# Approach:

# We will use three sets of data structures to keep track of the values we encounter in rows, columns, and sub-grids.

For each filled cell, we'll check:
If the value already exists in the corresponding row set.
If the value already exists in the corresponding column set.
If the value already exists in the corresponding 3x3 sub-grid set.
If any of the conditions fail, the board is invalid, and we return false.
If we traverse the entire board without any issues, the board is valid, and we return true.