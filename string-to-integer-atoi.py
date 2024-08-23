class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        i, n, sign, result = 0, len(s), 1, 0
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result

# Approach:
# Ignore Leading Whitespaces: We will skip any leading whitespace characters until we encounter the first non-whitespace character.

Check for Sign: After skipping the whitespaces, we need to check if the next character is either '-' (negative) or '+' (positive). If neither is present, we assume the number is positive by default.

Read the Digits: After determining the sign, we will read the digits from the string until we encounter a non-digit character or reach the end of the string.

Handle Overflow: We need to make sure that the number we construct does not exceed the 32-bit signed integer range. If it does, we will return INT_MAX (2147483647) or INT_MIN (-2147483648) depending on the sign.

Return the Result: Once the number is constructed, apply the sign and return the final result.