

'''
Hard Variant of Sliding Window
Brute Force, generate all windows and get global max freq
'''

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        max_match = 0

        for i in range(n - 1, -1, -1):
            current_match = 1
            temp_k = k
            for j in range(i - 1, -1, -1):
                if nums[i] - nums[j] <= temp_k:
                    current_match += 1
                    temp_k -= nums[i] - nums[j]
                else:
                    break
            max_match = max(max_match, current_match)
        return max_match

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# sliding window based solution, non-trivial
# Really hard, took me hours to come up
# idea is simple, as we sorted (non-increasing), we can spend k on futuer elements
#
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:

        nums = sorted(nums)[::-1]
        print(nums)
        n = len(nums)
        i = 0
        j = 0
        max_freq = 1
        current = 0
        while j < n:
            current += nums[j]
            while current + k < nums[i] * (j - i + 1):
                current -= nums[i]
                i += 1
            max_freq = max(max_freq, j - i + 1)
            j += 1

        return max_freq

# time complexity: O(n)
# Space Complexity
