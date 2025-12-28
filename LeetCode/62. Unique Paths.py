# Top down recursive dp with memoization
# Define recursive base case
# Handle out of bounds
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp  = [[None for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        def ways(i, j):
            # Base Case
            if i == 0 and j == 0:
                return dp[0][0]
            # bound check
            if i < 0 or j < 0:
                return 0
            # memo
            if dp[i][j] != None:
                return dp[i][j]
            else:
                # Recurrence relation
                dp[i][j] =  ways(i - 1, j) + ways(i, j - 1)
                return dp[i][j]
        
        
        return ways(m - 1, n - 1)

# Time complexityz: O(M*N)
# Space Complexity: O(M*N) //Also + O(M+N) recursion depth

# Iterative solution
# Same as 64, just dp state table info is different
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp  = [[None for n in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top_paths = dp[i - 1][j] if i > 0 else 0
                left_paths = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = top_paths + left_paths
        return dp[m - 1][n - 1]
        
        