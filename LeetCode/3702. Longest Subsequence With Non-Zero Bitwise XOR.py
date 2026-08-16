


'''
Initial DP based Solution, The very first was more worse, it was Backtrack withn exponential Complexity
This one a bit better, still MLE
The XOR range is too High to cache, its 10^9 max range !
Without caching, we go upto 2^N Complexity
'''
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        @cache
        def backtrack(position, xor) -> int:

            if position >= len(nums):
                if xor == 0:
                    return -math.inf
                else:
                    return 0

            # Take Current One
            xor_ = xor ^ nums[position]
            take = 1 + backtrack(position + 1, xor_)
            # Skip
            skip = backtrack(position + 1, xor)

            return max(take, skip)

        res = backtrack(0, 0)
        return max(res, 0)
# Time Complexity: n*2^30
# Space Complexity: n*2^30, MLE

'''
Bitwise Trick Based Solution
'''


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        xor = 0

        for num in nums:
            xor ^= num
        if xor != 0:
            return len(nums)
        for num in nums:
            if xor ^ num != 0:
                return len(nums) - 1

        return 0
# Time Complexity: O(n)
# Space Complexity: O(1)