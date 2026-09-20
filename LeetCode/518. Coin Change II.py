'''
Top Down Recursive Version + Memoization
'''


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        @cache
        def dp(remain, i) -> int:
            if remain == 0:
                return 1
            if remain < 0 or i >= len(coins):
                return 0

            return dp(remain - coins[i], i) + dp(remain, i + 1)

        return dp(amount, 0)

# Time Complexity: State Space: O(amount * n) where n = len(coins)
# Space Complexity: O(m*n)

'''
Iterative Version, had to take a sleep and solve next day, tried till 4am last night
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1
        # We cannot go over same coins again and again, that will create permutation, we want combination
        # That's why we go over coin, add it. If some future amount is reachable we add the coin again
        # This takes care of adding none to any times upto we reach amount
        for coin in coins:
            for i in range(amount):
                if dp[i] > 0 and i + coin < len(dp):
                    dp[i + coin] += dp[i]
        return dp[amount]

# Time Complexity: O(amount * n) where n = no of coins
# Space: O(amount)