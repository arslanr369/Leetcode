class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        reversed_number = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            digit = x % 10
            x //= 10
            
            if reversed_number > INT_MAX // 10 or (reversed_number == INT_MAX // 10 and digit > 7):
                return 0  
            
            reversed_number = reversed_number * 10 + digit
        
        return sign * reversed_number

# Approach:

# Extract Digits:

# We can extract the last digit of the number using the modulus operation (x % 10).
# After extracting a digit, we reduce the number by dividing it by 10 (using integer division).

# Construct the Reversed Number:

# Start with reversed_number = 0.
# Iteratively multiply reversed_number by 10 and add the extracted digit to build the reversed number.

# Check for Overflow:

# Before adding the next digit to reversed_number, we need to check if appending the digit would cause an overflow beyond the 32-bit integer range.
# Specifically, if reversed_number > 214748364 (since appending any digit to this would exceed 2147483647), or if reversed_number == 214748364 and the next digit is greater than 7, we should return 0 (since that would exceed the 32-bit signed integer limit).

# Handle Negative Numbers:

# We can handle negative numbers by keeping track of the sign of the original number, then reversing its absolute value, and finally applying the sign to the reversed result.