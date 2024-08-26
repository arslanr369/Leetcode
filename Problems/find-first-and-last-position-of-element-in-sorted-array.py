class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper function to find the first occurrence of target
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first_occurrence = mid  # Potential first occurrence
                    right = mid - 1  # Continue searching in the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence
        
        # Helper function to find the last occurrence of target
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last_occurrence = mid  # Potential last occurrence
                    left = mid + 1  # Continue searching in the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence
        
        # Find the first and last occurrences
        first = findFirst(nums, target)
        if first == -1:  
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]
