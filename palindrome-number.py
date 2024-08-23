class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10

# Approach:

# Negative Number Check: If x is negative, return false.

Edge Case for Last Digit Zero: If x ends with a 0 and x is not 0, return false.
Reversing Half of the Number: Reverse the second half of the digits. If the reversed half equals the first half, then the number is a palindrome.