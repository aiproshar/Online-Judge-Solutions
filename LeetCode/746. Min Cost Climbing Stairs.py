'''
Top down recursive dp + memoization
1. Objective function
2. Base Case
3. Recurrence Relation
4. Order of Computation
5. Where is the answer
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        # 1. Objective Function: dp(x) -> cost to arrive at x, not jump from x
        # That means base case arrivals cost is 0 , this is edge case
        def dp(n):
            # 2. Base Case
            if n < 2:
                return 0
            # 3. RR
            return min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
        # 4. Order of computation, top Down for recursive dp
        # 5. Where is answer
        return dp(n)
# Time Complexity: O(n) due to memoization
# Space Complexity: O(n) recursion depth



'''
Iterative version and advanced iterative version (constant space)
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # n+1 because we want to go over the stair
        dp = [0] * (n + 1)
        # dp[n] means cost to be in that step. Base case/ starting point has a cost 0
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]


# Time Complexity: O(n)
# Space complexity: O(n), no recursion risk

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