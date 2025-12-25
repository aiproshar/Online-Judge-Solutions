
# Recursive naive approach
# Dumbfuck approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def min_cost(cost: list[int], n: int):
            if n in (0, 1):
                return cost[n]
            return cost[n] + min(min_cost(cost, n-1), min_cost(cost, n-2))
        n = len(cost)
        return min(min_cost(cost, n-1), min_cost(cost, n-2))
# Time Complexity: Max Depth n, binary balanced tree, so 2^n
# Space complexity: Recursion stack O(n)       


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [None for _ in range(n)]

        dp[0] = cost[0]
        dp[1] = cost[1]

        for k in range(2, n):
            dp[k] = min(dp[k -1], dp[k - 2]) + cost[k]
        
        # This is the most important part
        # Corner Case
        # We can reach final state from two previous state
        # Optimization dp, we must calculate this
        # There are n stairs, but our final step is N + 1, the upper floor
        # so we compare best path from n and n-1 (n-1 and n-2 for 0 based indexing)
        return min(dp[n-1], dp[n-2])

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