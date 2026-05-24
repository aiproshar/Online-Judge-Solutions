# Most interview friendly solution
# Merge on linear time, find median on constant time, merge in a way that merged array is also sorted
# There is a constant space log(m+n) solution, which is extremely difficult and just checks if you can memorize solution
# I am avoiding that path and stick with optimal merge linear solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged_list = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged_list.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged_list.append(nums2[j])
            j += 1
        n = len(merged_list)
        if n % 2 == 0:
            n = n // 2
            return (merged_list[n] + merged_list[n-1]) / 2
        else:
            n = n // 2
            return merged_list[n]

# Time and Space complexity: O(n) linear