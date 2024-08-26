from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                    
                    if right - left == total_len:
                        result.append(left)
                
                else:
                    current_count.clear()
                    left = right
        
        return result

# Approach:

# Length Calculations:

# Each word in words has the same length word_len.
# The length of the concatenated substring would be total_len = word_len * len(words).

# Sliding Window:

# We slide over the string s and check each possible substring of length total_len.
# For each substring, we split it into words of length word_len and check if all the words match the required count from the list words.

# Using a Hashmap:

# We can use a hashmap to store the frequency of each word in words.
# For each substring, we check if we can match the required frequency of each word using another hashmap.
Edge Case:

If the total length of the concatenated string exceeds the length of s, return an empty list immediately.