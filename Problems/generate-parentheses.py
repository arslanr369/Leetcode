class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        # Helper function for backtracking
        def backtrack(current_string, open_count, close_count):
            # If the current string is a valid sequence with all pairs
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Add an opening parenthesis if we have any left to add
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)
            
            # Add a closing parenthesis if it's valid to do so
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)
        
        # Start the backtracking process
        backtrack("", 0, 0)
        
        return result
