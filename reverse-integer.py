class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Initialize reversed_number to 0
        reversed_number = 0
        
        # Remember the sign of x
        sign = -1 if x < 0 else 1
        
        # Work with the absolute value of x
        x = abs(x)
        
        # Process each digit of x
        while x != 0:
            # Extract the last digit
            digit = x % 10
            # Reduce x by removing the last digit
            x //= 10
            
            # Check for overflow before adding the digit
            if reversed_number > INT_MAX // 10 or (reversed_number == INT_MAX // 10 and digit > 7):
                return 0  # Overflow case, return 0
            
            # Build the reversed number
            reversed_number = reversed_number * 10 + digit
        
        # Return the reversed number with the appropriate sign
        return sign * reversed_number
