class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Use dictionaries to store the sets for rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                # If the cell is empty, skip it
                if board[i][j] == '.':
                    continue
                
                num = board[i][j]
                
                # Calculate the box index
                box_index = (i // 3) * 3 + (j // 3)
                
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        return True
