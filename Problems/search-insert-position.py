class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
# Approach:

# Binary Search:

# Start with two pointers, left and right, representing the bounds of the search space.

# Calculate the mid index and compare nums[mid] with the target.

# If nums[mid] is equal to the target, return mid.
# If nums[mid] is less than the target, narrow the search to the right half of the array.
# If nums[mid] is greater than the target, narrow the search to the left half of the array.
# Continue this process until the left pointer surpasses the right pointer.
# If the target is not found, the left pointer will point to the position where the target should be inserted.