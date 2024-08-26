class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == target else -1
    
# Explanation:
# Initial Setup: We initialize two pointers, left and right, to the beginning and end of the array, respectively.
# Binary Search Loop: The loop continues until the left pointer surpasses the right pointer.
# Check Mid Element: If nums[mid] equals the target, return mid.
#Left Half Sorted: If nums[left] <= nums[mid], it means the left half is sorted. We then check if the target is within that range to decide which half to search next.
#Right Half Sorted: If nums[mid] <= nums[right], it means the right half is sorted. Similarly, we check if the target is within that range.
#Return Value: If the target is not found, return -1.