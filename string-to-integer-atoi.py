class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        i, n, sign, result = 0, len(s), 1, 0
        
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for optional sign character
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Convert digits to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle overflow by checking the next possible value
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Apply the sign and return the result
        return sign * result
