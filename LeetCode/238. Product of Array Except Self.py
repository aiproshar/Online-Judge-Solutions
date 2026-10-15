'''
Non-inclusive prefix, suffix
non-inclusive reduces complexity, removes the need for sentinels and other edge case handling
non-inclusive means prefix[i] = nums[0] * nums[1]. .... nums[i-1] . Note nums[i] not included
The problem forbids using division operator, non-inclusive also takes care of that
Same for suffix
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        # Base Cases, prefix for start and suffix for last element imaginary extended array with invariant value (1)
        prefix[0] = 1
        suffix[-1] = 1
        # non-inclusive
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Reduces down complexity
        res = [prefix[i] * suffix[i] for i in range(n)]

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)