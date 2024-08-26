class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# Explanation:
# Finding the first decreasing element: We start from the rightmost element and look for the first pair where nums[i] < nums[i + 1]. This step helps identify where the array can be modified to find the next permutation.

Finding the element to swap: After identifying the first decreasing element, we find the smallest element larger than nums[i] to ensure the smallest lexicographical increment.

Swapping: We swap the identified elements to create a new permutation.

Reversing the suffix: Reversing the portion of the array after the swapped element gives the smallest possible permutation with the modified prefix.