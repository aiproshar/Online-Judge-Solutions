
# Recursive naive approach
# Dumbfuck approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def dp(i) -> int:
            if i == 0 or i == 1:
                return 0
            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
        return dp(n)
# Time Complexity: Max Depth n, binary balanced tree, so 2^n
# Space complexity: Recursion stack O(n)       


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # n+1 because we want to go over the stair
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


# Time Complexity: O(n)
# Space complexity: O(n)

# Follow Up -> Can you do this in reduced space complexity ?
# Remember, anything reduced than linear is constant
# We just need the previous 2 states to go to the next state, 
# Remember MIT 6006 -> everydp bottom up is a DAG topological sort, 
# to calculate state n if we need constant previous state, we can always do this in constant time


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        x = cost[0]
        y = cost[1]

        for k in range(2, n):
            tmp = min(x, y) + cost[k]
            x = y
            y = tmp

        return min(x, y)
# Improved space complexity: O(1)