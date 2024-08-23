class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result

# Approach:
# Sorting: First, we sort the array to simplify the process of finding triplets and avoiding duplicates.
# Two-pointer technique: For each number in the array, treat it as a fixed number and use the two-pointer technique 
# to find two other numbers that together with the fixed number sum to zero.
# Avoid Duplicates: As we are looking for unique triplets, we skip duplicates in both the fixed number and the two-pointer part.
