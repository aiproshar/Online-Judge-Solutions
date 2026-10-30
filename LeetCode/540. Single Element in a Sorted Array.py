class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums)
        while lo < hi:
            bumped = False
            mid = (lo + hi) // 2
            if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                mid += 1
                bumped = True
            if (mid - lo + 1) % 2 == 0:
                lo = mid + 1
                # skipping infinite loop when we have 3 items
                hi = mid - 2 if bumped else mid
        return nums[lo]

# Time Complexity: O(logn)
# Space Complexity: O(n)