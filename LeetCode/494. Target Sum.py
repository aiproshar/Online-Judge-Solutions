'''
Top Down Recursive Approach
We have two choices for each number, we take positive of it or negative of it
No early termination, no pruning. We must take all the numbers, only compare when we in exit leaf
@cache for memo, 2D dp state table
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dp(idx, state) -> int:
            if idx == len(nums):
                if state == target:
                    return 1
                else:
                    return 0
            return dp(idx + 1, state + nums[idx]) + dp(idx + 1, state - nums[idx])

        return dp(0, 0)
# Time Complexity: n * S , where n = len(nums) ,  S is range of all possible partial to full sums.
# Its usually -sum(nums) to +sum(nums) or 2S-1 state, we can say it as S

# Space Complexity: O(n*s) + O(n) recursion stack
# Drawback with all recursion: Stack Overflow

'''
Iterative Approach
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(lambda: 0)
        dp[0] = 1
        for num in nums:
            temp = defaultdict(lambda: 0)
            for key in dp.keys():
                temp[key + num] += dp[key]
                temp[key - num] += dp[key]
            dp = temp
        return dp[target] # we will have mutation here

# Time Complexity: O(n*S)
# Space Complexity: -sum(n) to +sum, 2s-1 so O(s)