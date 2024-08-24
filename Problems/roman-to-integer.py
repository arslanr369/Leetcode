class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total += roman_values[s[i + 1]] - roman_values[s[i]]
                i += 2  
            else:
                total += roman_values[s[i]]
                i += 1
        
        return total


# Algorithm:
# Traverse the string from left to right.
# If the current symbol has a smaller value than the next symbol, subtract its value.
Otherwise, add its value to the total.
Continue this process until the end of the string.