class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  
        
        def backtrack(remaining, combination, start):
            if remaining == 0:
                result.append(list(combination))
                return
            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                combination.append(candidates[i])
                backtrack(remaining - candidates[i], combination, i + 1)
                combination.pop()
        
        backtrack(target, [], 0)
        return result

# Approach:

# Backtracking:

# Use backtracking to explore all possible combinations of candidates that sum to the target.
# Unlike the previous problem, here you can't reuse the same element. Thus, move to the next element after including the current one.
# Sort the array to handle duplicates easily.

# Handling Duplicates:

# After sorting the candidates, skip duplicate numbers when iterating to ensure that each combination is unique.