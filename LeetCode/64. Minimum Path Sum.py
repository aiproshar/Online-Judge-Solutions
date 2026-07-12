

'''
Top Down Recursive Approach
1. Objective Function: F(x,y) -> minimum cost to come to x,y position. We memoize this
2. Base Case: F(0,0) -> This is start point, only the grid cost is here
3. Recurrence Relation: F(x,y) = min{F(x-1, y) , F(x, y-1)} + cost[x][y]
4. Order Of Computation: 0,0 -> m-1, n-1
5. Location: dp[m-1, n-1]
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(x, y) -> int:
            if x == 0 and y == 0:
                return grid[0][0]
            if x < 0 or y < 0:
                return math.inf
            return min(dp(x - 1, y), dp(x, y - 1)) + grid[x][y]

        return dp(len(grid) - 1, len(grid[0]) - 1)

# Time Complexity: O(m*n) total DP state Space
# Space Complexity: O(m*n) for State Space Cache + O(m+n) for recursion depth

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


        