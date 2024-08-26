class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurrence = mid  
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurrence = mid  
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence
        
        first = findFirst(nums, target)
        if first == -1:  
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]

# Approach:
# Binary Search for the First Occurrence:

# Perform a binary search that narrows down the search to find the first position where the target appears in the array.
# When the middle element matches the target, continue searching in the left half of the array to ensure you find the first occurrence.
# Binary Search for the Last Occurrence:

# Similarly, perform a binary search that narrows down the search to find the last position where the target appears in the array.
# When the middle element matches the target, continue searching in the right half of the array to ensure you find the last occurrence.
# If the target is not found in the array, return [-1, -1].