'''
bisect based standard solution, this is what we must do

'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        left_idx = bisect.bisect_left(nums, target)
        right_idx = bisect.bisect_right(nums, target)

        # if left idx valid, means the number exists and also that means right_idx also valid
        if left_idx < len(nums) and nums[left_idx] == target:
            return [left_idx, right_idx - 1]
        else:
            return [-1, -1]

# Time Complexity: O(logn)
# Space: O(1)