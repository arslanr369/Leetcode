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
                # Recursively call backtrack with the updated remaining sum
                backtrack(remaining - candidates[i], combination, i)
                # Backtrack, remove the last added element
                combination.pop()
        
        candidates.sort()  
        backtrack(target, [], 0)
        
        return result
