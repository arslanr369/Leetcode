class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  
        
        return closest_sum

# Explanation:

# Sorting: Sorting the array helps in efficiently moving the two pointers to find the closest sum.

Two Pointers Technique: For each element in the array, use two pointers to explore possible sums with the remaining elements. Adjust the pointers based on whether the current sum is less than or greater than the target.

Update Closest Sum: Compare the absolute difference between the current sum and the target with the closest sum found so far and update if necessary.