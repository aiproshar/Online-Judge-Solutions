
# TOP DOWN with memoization
# REcursive dp

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        ROW = len(grid)
        COL = len(grid[0])
        dp = [[INF for _ in range(COL)] for _ in range(ROW)]

        dp[0][0] = grid[0][0]

        def path_sum(i, j):
            # Base case
            if i == 0 and j == 0:
                return grid[0][0]
            # Bound Check
            if i < 0 or j < 0:
                return INF
            # Memoization, reduces time complexity from 2^(m+n) to m*n (exponential to polynomial)
            if dp[i][j] != INF:
                return dp[i][j]
            up_sum = path_sum(i - 1, j)
            left_sum = path_sum(i, j - 1)

            dp[i][j] = min(up_sum, left_sum) + grid[i][j]
            return dp[i][j]
        
        
        min_cost = path_sum(ROW - 1, COL - 1)
        return min_cost

            
        

# 2D basic dp table
# Forward dp, iterative
# some states are out of bound, as this is a minimization problem, we initiate out of bounds with INF
# The most important part is realizing, all our previous state is computed which upon we can come into current state
# Thats why we can access the dp table easily
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        dp = [[INF for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                up_min = dp[i - 1][j] if i - 1 >= 0 else INF
                left_min = dp[i][j - 1] if j - 1 >=0 else INF
                dp[i][j] = grid[i][j] + min(left_min, up_min)
        return dp[len(grid) - 1][len(grid[0]) - 1]
            
# Time complexityt: O(m*n)
# Space: O(m*n)


        