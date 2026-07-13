# Top down recursive dp with memoization
# Define recursive base case
# Handle out of bounds
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dp(i, j) -> int:
            if i == 0 and j == 0:
                return 1

            if i < 0 or j < 0:
                return 0

            return dp(i - 1, j) + dp(i, j-1)

        return dp(m - 1, n - 1)

# Time Complexity: O(M*N) [state space]
# Space Complexity: O(M*N) //Also + O(M+N) recursion depth





# Iterative solution
# Same as 64, just dp state table info is different
from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = dp[i-1][j] if i - 1 >= 0 else 0
                left = dp[i][j-1] if j - 1 >= 0 else 0
                dp[i][j] = top + left
        return dp[m-1][n-1]

# Time complexity: O(M*N)
# Space complexity: O(m*N)
