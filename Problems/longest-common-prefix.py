class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
# Algorithm:

# Start with the first string as the initial prefix.
# Iterate through the rest of the strings in the array, updating the prefix by comparing it with each string.
# For each string, reduce the prefix character by character until it matches the beginning of the current string.
# If at any point the prefix becomes an empty string, return an empty string as there is no common prefix.