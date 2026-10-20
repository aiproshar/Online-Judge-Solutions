'''
Easy but bit different

We are interested in invalid state, not valid state
Update global state in invalid state
'''


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        min_len = math.inf
        i = j = 0
        n = len(nums)
        current = 0

        while j < n:

            current += nums[j]
            # invalid state is what we interested in
            while current >= target:  #
                min_len = min(min_len, j - i + 1)
                current -= nums[i]
                i += 1
            j += 1

        return 0 if min_len == math.inf else min_len

# Time Complexity: O(n)
# Space Complexity: O(1)