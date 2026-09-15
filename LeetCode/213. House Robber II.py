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
        @cache
        def dp(i, money) -> int:
            if i == 0:
                return money[0]
            if i == 1:
                return max(money[0], money[1])
            return max(money[i] + dp(i-2, money), dp(i-1, money))
        first = tuple(nums[0:-1])
        last = tuple(nums[1:])
        return max(dp(len(first) - 1, first), dp(len(last) - 1, last))

# Time Complexity: O(n) calls, each call due to tuple hashing, takes O(n^2), and this is a trap
# When you use @cache you must think how much time it takes to hash the params, O(1) it should be


#  Optimized wrapper
# So we don't need to pass the list/tuple and cache it
# Closure Pattern
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def wrapper(money):
            @cache
            def dp(i) -> int:
                if i == 0:
                    return money[0]
                if i == 1:
                    return max(money[0], money[1])
                return max(money[i] + dp(i-2), dp(i-1))
            return dp(len(money) - 1)
        return max(wrapper(nums[1:]), wrapper(nums[:-1]))

# Time Complexity: O(n)
# Space: O(n) recursion depth, call stack overflow risk

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