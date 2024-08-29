class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the number at its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1

# Approach:

# Understanding the Problem:

# The smallest missing positive integer must be in the range [1, len(nums) + 1].
# If all numbers from 1 to len(nums) are present in the array, the answer will be len(nums) + 1.
In-Place Rearrangement:

We can use the array itself to track whether a number in the range [1, len(nums)] is present.
The idea is to place each number x in its correct position at index x - 1. For example, if x = 3, place it at index 2.
We iterate over the array and swap numbers to their correct positions.
Final Check:

After rearranging, we iterate through the array again. The first index i such that nums[i] != i + 1 will give the missing positive integer, which is i + 1.
If no such index is found, return len(nums) + 1.