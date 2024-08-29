class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Lengths of input string s and pattern p
        n, m = len(s), len(p)
        
        # DP table with (n + 1) rows and (m + 1) columns initialized to False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Base case: Empty string and empty pattern match
        dp[0][0] = True
        
        # Fill the first row (pattern with empty string s)
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        
        # The answer is whether the entire string matches the entire pattern
        return dp[n][m]

# Example usage:
solution = Solution()
print(solution.isMatch("aa", "a"))      # Output: False
print(solution.isMatch("aa", "*"))      # Output: True
print(solution.isMatch("cb", "?a"))     # Output: False
print(solution.isMatch("adceb", "*a*b"))# Output: True
print(solution.isMatch("acdcb", "a*c?b")) # Output: False


# Approach:
# We can use dynamic programming (DP) to solve this efficiently. Let dp[i][j] represent whether the substring s[0:i] matches the pattern p[0:j].

# DP Transition Rules:
# Base Case:

# dp[0][0] = True: Both string s and pattern p are empty, so they match.
# dp[i][0] = False for all i > 0: A non-empty string cannot match an empty pattern.
# dp[0][j]: This is True if the pattern p contains only * characters up to j.
# Filling the DP Table:

# If p[j-1] == '?', it matches any single character, so dp[i][j] = dp[i-1][j-1].
# If p[j-1] == '*', it can match zero characters (dp[i][j-1]) or any sequence of characters (dp[i-1][j]). Thus, dp[i][j] = dp[i][j-1] || dp[i-1][j].
# If p[j-1] == s[i-1], they match, so dp[i][j] = dp[i-1][j-1].
# Otherwise, dp[i][j] = False.
# Complexity:
# Time Complexity: O(n * m), where n is the length of s and m is the length of p.
# Space Complexity: O(n * m) for the DP table.