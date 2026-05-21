class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        # Narrow search space until two elements remain
        while lo < hi - 1:
            mid = (lo + hi) // 2

            # If mid > hi, min must be in right half
            if nums[mid] > nums[hi]:
                lo = mid
            # Otherwise, min is at mid or to its left
            else:
                hi = mid

        # lo and hi are adjacent (or equal); min is one of them
        return min(nums[lo], nums[hi])
# Time complexity: O(lgN)
# Space complexity: O(1)