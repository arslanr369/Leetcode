class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = total_left - i
            
            # nums1[i-1] <= nums2[j] and nums2[j-1] <= nums1[i]
            if i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            else:
                # Correct partition found
                max_left = 0
                if i == 0: 
                    max_left = nums2[j - 1]
                elif j == 0: 
                    max_left = nums1[i - 1]
                else: 
                    max_left = max(nums1[i - 1], nums2[j - 1])
                
                if (m + n) % 2 == 1:
                    return max_left
                
                min_right = 0
                if i == m: 
                    min_right = nums2[j]
                elif j == n: 
                    min_right = nums1[i]
                else: 
                    min_right = min(nums1[i], nums2[j])
                
                return (max_left + min_right) / 2.0
