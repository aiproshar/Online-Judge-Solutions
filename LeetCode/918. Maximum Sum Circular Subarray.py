class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        max_sum = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            # continue expand or start fresh, kadanes algorithm
            current = max(current + nums[i], nums[i])
            max_sum = max(max_sum, current)

        # split
        # find the minimum subarray, as the dip. Then we remove it from the total sum
        current = nums[0]
        min_sum = nums[0]
        for i in range(1, len(nums)):
            # continue expand or start fresh, kadanes algorithm but we wind minimum
            current = min(current + nums[i], nums[i])
            min_sum = min(min_sum, current)
        # corner case, our dip is the whole array, and we must take at least one element
        if min_sum != sum(nums):
            # dip is not the whole array
            max_sum = max(max_sum, sum(nums) - min_sum)

        return max_sum
