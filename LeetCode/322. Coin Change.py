class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        # 1. Objective Function: How many minimum needed to make x amount
        @cache
        def dp(left) -> int:
            # 2. base case, nothing left. We made up amount
            if left == 0:
                return 0
            # 2. Impossible to made up, return inf
            if left < 0:
                return math.inf
            res = []
            for coin in coins:
                res.append(dp(left - coin))
            # 3. Recurrence Relation. Optimization. From all brancehs, take the smallest one
            # Add one as we used one coin in current branch
            return min(res) + 1

        # 4. Order of computation: Top Down recursive DFS
        # 5. Where is answer ? Need to calculate this for amount, plug amount on objective function
        return dp(amount) if dp(amount) != math.inf else -1

# Time Complexity: O(amount) * S, where S = len(coins)
# Space Complexity: Recursion Depth, amount / min(cost). Cache takes O(amount)




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