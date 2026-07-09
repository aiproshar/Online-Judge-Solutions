# Recursive version with memoization
# Our state: How much space left, return how many ways we can fill that space
# Two Theoretical value, INF and None
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(weight) -> int:
            if weight == 0:
                return 0
            if weight < 0:
                return math.inf
            res = []
            for coin in coins:
                res.append(dp(weight - coin))
            return min(res) + 1

        mn = dp(amount)
        if mn == math.inf:
            return -1
        return mn

# Time complexity: O(amount * coins)
# Space complexity: O(amount + coins) //amount -> dp table, coin -> recursion depth




# Iterative version
# We must thing what can be done to come to current state, so that we can reuse previous state computations
# We computing dp[10], means how can we come to dp[12] state, obviously adding coins. So we want to
# have a 5 usd coin, so we need 12-5 = 7, we can use whats computed on dp[7] and come to dp[12] by adding 5
# We iterate all the previous possible state from where we can come to current state, take the min value (optimization)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == math.inf:
            dp[amount] = -1
        return dp[amount]

# Time Complexity: O(amount * coins) // Two for loops
# Space complexity: O(amount) //improvement over recursive and also no risk of stack overflow