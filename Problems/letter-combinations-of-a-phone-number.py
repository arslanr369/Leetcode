class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index, current_combination):
            if index == len(digits):
                combinations.append(current_combination)
                return
            letters = phone_map[digits[index]]
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        
        return combinations

# Approach:
# Handle Edge Cases: If the input string is empty, return an empty list.
Backtracking: Use a backtracking approach to generate all combinations by recursively selecting letters for each digit.