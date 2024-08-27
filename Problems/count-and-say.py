class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def next_sequence(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count))
                result.append(s[i])
                i += 1
            return ''.join(result)
        
        current = "1"
        for _ in range(n - 1):
            current = next_sequence(current)
        
        return current

# Approach:

# We will iteratively build the sequence from countAndSay(1) up to countAndSay(n).

Start with the base string "1".
For each step, generate the next string by reading off the previous string (using the run-length encoding approach).
Continue this until we reach the nth string.