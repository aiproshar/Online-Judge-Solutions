# Recursive top down DP
# GOT TLE in leetcode
class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n):
            if n in {1,2}:
                return n
            return stairs(n-1) + stairs(n-2)
        return stairs(n)
# Time complexity 2^n (Binary balanced tree, depth n)
# Space complexity: O(n) -> Max recursion depth


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

# Time and space complexity: O(n)
# Follow Up :-> can you do this is constant space ?


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        # Memoization

        # Base Case
        x = 1
        y = 2
        temp = 0
        for k in range(3, n + 1):
            # Recurrance Relation
            temp = x + y
            x = y
            y = temp 
        return temp

# Improved space complexity O(1)