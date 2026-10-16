'''
Standard brute Force Solution
Walk through every possible subet, and which meets condition do stuffs
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_len = 0
        n = len(nums)
        for i in range(n):
            zero_count = 0
            one_count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zero_count += 1
                elif nums[j] == 1:
                    one_count += 1

                if zero_count == one_count:
                    max_len = max(max_len, j - i + 1)
        return max_len
# Time Complexity: O(n^2)
# Space Complexity: O(1)




class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_len = 0
        n = len(nums)

        deltas = {0: -1}

        ones = 0
        zeros = 0

        for i, num in enumerate(nums):
            if num == 1:
                ones += 1
            else:
                zeros += 1
            delta = ones - zeros
            if delta in deltas:
                len_ = i - deltas[delta]
                max_len = max(max_len, len_)
            else:
                deltas[delta] = i
        return max_len

