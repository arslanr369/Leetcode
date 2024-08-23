class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1, the pattern is just the original string
        if numRows == 1:
            return s
        
        # Initialize a list of strings for each row
        rows = [''] * min(numRows, len(s))
        
        # Variables to track the current row and direction (down or up)
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            # Add the character to the current row
            rows[current_row] += char
            
            # If we are at the top or bottom, reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row (down if going_down is True, up otherwise)
            current_row += 1 if going_down else -1
        
        return ''.join(rows)
