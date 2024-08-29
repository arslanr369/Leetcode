class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = mx = last = 0
        for i, x in enumerate(nums[:-1]):
            mx = max(mx, i + x)
            if last == i:
                ans += 1
                last = mx
        return ans

# Solution Explanation:
# Initialize Variables:

# jumps: to count the number of jumps.
# current_end: the farthest point reachable with the current number of jumps.
# farthest: the farthest point that can be reached with one more jump beyond current_end.
# Iterate through the array:

# For each index i, update the farthest point that can be reached.
# When i reaches current_end, it means you need to make a jump, so increment the jumps counter and update current_end to the farthest point.
# Termination:

# The loop runs until the second-last index because by the time you reach it, you will have made enough jumps to reach the last index.