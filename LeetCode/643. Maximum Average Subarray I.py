'''
Basic Sliding Window
'''
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        n = len(nums)
        if n <= k:
            return sum(nums) / k

        current = 0
        i = j = 0
        max_avg = -math.inf
        while j < n:
            current += nums[j]
            while j - i + 1 > k:
                current -= nums[i]
                i += 1
            if j - i + 1 == k:
                max_avg = max(max_avg, current / k)
            j += 1

        return max_avg
# Time Complexity: O(n)
# Space Complexity: O(1)