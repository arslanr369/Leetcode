class Solution:
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i)
                combination.pop()
        
        candidates.sort()  
        backtrack(target, [], 0)
        
        return result

# Approach:

# Backtracking:

# Start with an empty combination and a sum of 0.
# For each number in the candidates list, try to add it to the current combination.
# If the sum exceeds the target, stop exploring that path (backtrack).
# If the sum equals the target, add the current combination to the result.
# Recur by trying to add the current number again (since the number can be used multiple times).
# After exploring all possibilities, backtrack by removing the last added number and try the next number.

# Sorting:

# Sorting the candidates array can help to optimize the backtracking by stopping early if the sum exceeds the target.

# Avoiding Duplicates:

Ensure that each combination is unique by tracking the frequency of numbers in the combination.