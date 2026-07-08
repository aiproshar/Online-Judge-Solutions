# Almost same as House Robber

'''
Thought Process

My initial thought  was we can either have the first one or the last one, and we dont have any other choice
So lets break down the problem into two problems, excluding first one and excluding the last one
Also there was a corner case, where we have only one item, in that case i handled with hard code
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_partial(houses: list[int]) -> int:
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                rob = houses[i] + dp[i - 2]
                skip = dp[i - 1]
                dp[i] = max(rob, skip)
            return dp[-1]

        first = rob_partial(nums[0:-1])
        last = rob_partial(nums[1:])
        return max(first, last)

# Time Complexity: O(n)
# Space Complexity: O(n)