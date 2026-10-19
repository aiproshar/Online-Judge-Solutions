
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        i = j = 0
        max_len = 0
        # state
        zeros = 0
        while j < len(nums):
            # do state change
            if nums[j] == 0:
                zeros += 1
            # invalid state
            while zeros > k:
                # undo state change
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            # valid state
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''