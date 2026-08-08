'''
One-liner python merge
Not efficient
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[0:m] + nums2[0:n]
        temp.sort()
        nums1.clear()
        for x in temp:
            nums1.append(x)

# Time Complexity: O( m+n log m+n)
# Space Complexity: O(m+n)


'''
No sort method
Still takes up a bit extra memory
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        initial_len = len(nums1)

        i = j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums1.append(nums1[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        while i < m:
            nums1.append(nums1[i])
            i += 1
        while j < n:
            nums1.append(nums2[j])
            j += 1
        del nums1[:initial_len]
# Time and Space both: O(m+n)


'''
This is the most optimal one
No extra time and space complexity 
The idea is backfill, so there is no chance of overnight of existing items
This only works because nums1 is size of m_n
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1

        k = len(nums1) - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1
# Time: O(m+n0
# Space: O(1)

