class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - i - 1] = max(right[n - i], height[n - i - 1])
        return sum(min(l, r) - h for l, r, h in zip(left, right, height))

# Approach:

# Understanding the Problem:

# Water can only be trapped at a position if there is a taller bar both to the left and to the right of that position.
# The amount of water trapped at any given position is determined by the shorter of the tallest bars to the left and the right minus the height of the current bar.
Dynamic Programming Approach:

Left max array: We can create an array left_max where left_max[i] stores the tallest bar to the left of index i.
Right max array: Similarly, create an array right_max where right_max[i] stores the tallest bar to the right of index i.
Once we have these two arrays, the water trapped at each index i is min(left_max[i], right_max[i]) - height[i] if this value is positive.
Two-Pointer Approach (Optimal Solution):

Instead of using extra space for the left_max and right_max arrays, we can use two pointers (left and right) to scan the array from both ends.
We maintain two variables left_max and right_max to keep track of the maximum heights seen so far from the left and the right, respectively.
At each step, we calculate the water trapped based on the minimum of left_max and right_max, and move the pointer accordingly.