class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        
        return result
    
# Approach:

# Backtracking: We will use a recursive function to build the string of parentheses step by step. At each step, we decide whether to add an opening ( or closing ) parenthesis, ensuring that the string remains valid.
# Conditions:
We can only add an opening ( parenthesis if we haven't used all n opening parentheses.
We can only add a closing ) parenthesis if the number of closing parentheses is less than the number of opening parentheses (this ensures validity).
Base Case: When the current string of parentheses has 2*n characters (meaning all n pairs are placed), we add it to the result list.
