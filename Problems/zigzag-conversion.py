class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * min(numRows, len(s))
        
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            current_row += 1 if going_down else -1
        
        return ''.join(rows)
    
# Approach:
# Zigzag Pattern:

# The zigzag pattern involves writing the characters in a top-down fashion (column-wise), then diagonally up to the next column, repeating this process.
# Each row of the zigzag pattern collects certain characters from the input string.

# Simulation:

# We simulate this process by keeping track of the current row while iterating through the string.
# We move in a "downward" direction initially, and once we reach the bottom row, we switch to moving "upward". This process is repeated until the end of the string.

# Edge Case:

# If numRows is 1, the zigzag pattern is just the original string itself, so we can return the string as-is.
