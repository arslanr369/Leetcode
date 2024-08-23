class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
    
# Approach:
# Palindrome Characteristics:

# A palindrome reads the same forward and backward.
# The center of a palindrome can be either a single character (for odd-length palindromes) or a pair of identical characters (for even-length palindromes).
# Expand Around Center:

# For every character (and every pair of consecutive characters) in the string, we consider it as the center of a potential palindrome.
# We expand outwards while the characters on both sides are the same, keeping track of the longest palindrome found during this process.
# Efficiency:

# By expanding from each center, we effectively check for palindromes in O(n^2) time, which is efficient given the constraints.