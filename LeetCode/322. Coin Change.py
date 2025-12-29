# Recursive version with memoization
# Our state: How much amount left, value: how many ways on that amount
# Two Theoretical value, INF and None
# We could have gone with INF as initial value only, but INF can remain as INF if there is no path to solution
# So we use None and INF to distinguish non-explored and impossible
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        INF = float('inf')
        dp = [ None for _ in range(amount + 1) ]
        # dp tables preserves the amount left and stores the way to do it.
        # example, dp[20] = 7 means we can excahnge 20 with existing coins using minimum using 7 coins
        # base case, no coin count because no amount left
        dp[0] = 0

        def get_min(amount):
            #base case
            if amount == 0:
                return dp[0]
            if dp[amount] != None:
                #memoization
                return dp[amount]
            # selecting minimum from branching
            min_ways = INF
            for coin in coins:
                if amount - coin >= 0:
                    min_ways = min(min_ways, get_min(amount - coin))
            # Need to add plus one, our state keeps track of coins count.
            # Clause was crying to check if its INF we have no good adding +1 to INF
            '''
            @suggested change by claude opus 4.5
            dp[amount] = min_ways + 1 if min_ways != INF else INF
            '''
            # But python is too god, INF + 1 == INF in python YAY. More clean code
            dp[amount] = min_ways + 1
            return dp[amount]
        
        get_min(amount)


        if dp[amount] == INF:
            return -1
        return dp[amount]

# Time complexity: O(amount * coins)
# Space complexity: O(amount + coins) //amount -> dp table, coin -> recursion depth




# Iterative version
# We must thing what can be done to come to current state, so that we can reuse previous state computations
# We computing dp[10], means how can we come to dp[12] state, obviously adding coins. So we want to
# have a 5 usd coin, so we need 12-5 = 7, we can use whats computed on dp[7] and come to dp[12] by adding 5
# We iterate all the previous possible state from where we can come to current state, take the min value (optimization)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [None for _ in range(amount + 1)]
        #initial case
        dp[0] = 0

        # Going sequentially bottom up, means if we want to calculate current state, all previous states are computed
        for i in range(1, amount + 1):
            min_val = INF
            for coin in coins:
                # Bound checking, excluding invalid previous states
                if i - coin >= 0:
                    min_val = min(min_val, dp[i - coin])
            dp[i] = min_val + 1
        return dp[amount] if dp[amount] != INF else -1

# Time Complexity: O(amount * coins) // Two for loops
# Space complexity: O(amount) //improvement over recursive and also no risk of stack overflow