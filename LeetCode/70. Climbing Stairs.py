'''
Top down recursive dp + memoization
Standard Framework solution
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        # 1. Objective function: dp(x) -> ways to reach x position
        def dp(i):
            '''
            2. Base case:
            How many ways we can reach first step, only one way
            How many ways we can reach second step ? Two ways directly or via first stop
            so dp(1) = 1 and dp(2) = 2
            '''
            if i == 1 or i == 2:
                return i
            # 3. Recurrence Relation: How to calculate dp(i)
            # We can come to its step from previous two steps (i-1) and (i-2) by taking one and two steps
            # So combine them we can have the ways to reach current position
            return dp(i-1) + dp(i-2)
        # 4. Order of computation: Top Down so we start from n
        # Where is result: dp(n) returns the result to nth step AKA the top
        return dp(n)

    # Time Complexity: O(n)
    # Space Complexity: O(n) recursion stack


# Bottom Up iterative DP
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        # Memoization
        dp = [None for _ in range(n + 1)]

        # Base Case
        dp[1] = 1
        dp[2] = 2

        for k in range(3, n + 1):
            # Recurrance Relation
            dp[k] = dp[k - 1] + dp[k - 2]
        return dp[n]

# Time and space complexity: O(n), recursion stack overflow risk
# Follow Up :-> can you do this is constant space ?


class Solution:
    def climbStairs(self, n: int) -> int:
        # base case termination
        if n < 3:
            return n
        # very first previous element
        pre_first = 2
        # very second previous element
        pre_second = 1
        for i in range(3, n+1):
            temp = pre_first + pre_second
            pre_first, pre_second = temp, pre_first
        return pre_first
# Time Complexity: O(n)
# Improved space complexity O(1)