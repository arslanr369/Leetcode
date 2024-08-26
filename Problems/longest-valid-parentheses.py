class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

# Explanation:

# Stack Initialization: We push -1 initially to handle cases where the valid substring starts at the beginning of the string.
# Traversal:
# For each (, we push the index onto the stack.
For each ), we pop the stack and check if it’s empty. If it is, push the current index to reset the start of a new substring. Otherwise, calculate the length of the valid substring using the difference between the current index and the new top of the stack.
Updating Maximum Length: We continuously update the maximum length of valid substrings during the traversal.
Time Complexity:
The time complexity is O(n), where n is the length of the string, as we traverse the string once.
Space Complexity:
The space complexity is O(n) due to the use of the stack, which could store up to n indices in the worst case.