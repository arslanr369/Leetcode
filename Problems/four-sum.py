class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

# Approach:
# Sorting: Sort the array to facilitate the use of two pointers and help in skipping duplicates.

# Two Pointers: Iterate through the array using two nested loops for the first two numbers in the quadruplet. For the remaining two numbers, use two pointers (one starting from the left and one from the right) to find pairs that complete the quadruplet.

# Skipping Duplicates: To avoid duplicate quadruplets, skip over any repeated values during the iteration.

Time Complexity: The solution uses a four-level nested loop, but the innermost two loops are handled by the two-pointer approach. The overall time complexity is 
𝑂
(
𝑛
3
)
O(n 
3
 ), which is feasible given the constraints.