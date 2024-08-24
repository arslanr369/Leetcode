class Solution:
    def threeSumClosest(self, nums, target):
        # Step 1: Sort the array
        nums.sort()
        
        # Initialize the closest sum with a large value
        closest_sum = float('inf')
        
        # Step 2: Iterate through the array
        for i in range(len(nums) - 2):
            # Set two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                # Calculate the current sum
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
