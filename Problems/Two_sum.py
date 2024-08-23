class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # To store the complement and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
            
# Approach:
#Hash Map: We can iterate through the array while maintaining a hash map to store the difference between the target and the current number (i.e., target - nums[i]) as the key, and the current index as the value.
#Check for Complement: As we iterate through the array, for each number nums[i], check if it exists in the hash map (i.e., if its complement has been seen before). If it exists, we found the two numbers that add up to the target, and we return their indices.