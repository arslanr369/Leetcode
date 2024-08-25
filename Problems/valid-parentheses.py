class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold the opening brackets
        stack = []
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack



# Explanation:

# Stack: The stack stores opening brackets as we encounter them.
# Bracket Map: The bracket_map dictionary maps each closing bracket to its corresponding opening bracket. This allows us to quickly check for matches.

# Iterate through s:

# If the character is a closing bracket, check if the top of the stack is the corresponding opening bracket.
# If it is, pop the stack; if not, return False (the string is invalid).
If the character is an opening bracket, push it onto the stack.
Final Check: After iterating through the string, if the stack is empty, the string is valid. If there are unmatched opening brackets left in the stack, the string is invalid.