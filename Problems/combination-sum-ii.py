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
