
#basic iterative binary search
# corner case: lo <= hi (not strict less)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
        return -1



# non-trivial recursive solution
# Just for example
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        def bi_search(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return bi_search(mid+1, hi)
            elif target < nums[mid]:
                return bi_search(lo, mid-1)
        return bi_search(lo, hi)

# Python Build In bisect library
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        position = bisect_left(nums, target)
        if position < len(nums) and nums[position] == target:
            return position
        else:
            return -1
