class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  
        left = 0  
        max_length = 0  
        
        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            
            char_index_map[char] = right
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Approach:
# Sliding Window:

# We maintain a window that expands as we traverse the string, checking for unique characters.
# If a character is repeated within the window, we shrink the window from the left to remove the repeated character, ensuring that the window always contains unique characters.
# Hash Map:

# We use a hash map to store the most recent index of each character in the string.
# If a character is found that is already in the hash map and its index is within the current window, we update the starting position of the window to the right of this character's last occurrence.
# Update Maximum Length:

# Throughout the process, we continuously update the maximum length of the substring found without repeating characters.