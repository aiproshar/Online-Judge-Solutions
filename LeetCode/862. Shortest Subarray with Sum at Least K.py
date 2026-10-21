
'''
Got Beaten Up Badly, unable to solve optimally
Current Solution TLE, Generate all subarray bruteforce + pruning
'''


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:

        n = len(nums)
        min_len = math.inf
        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                if current >= k:
                    min_len = min(min_len, j - i + 1)
                    # future subarrays will be larger,early exit
                    break

        return min_len if min_len != math.inf else -1
# TC: O(n^2)
# SC: O(1)