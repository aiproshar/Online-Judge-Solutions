class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0

        @cache
        def dp(i, j) -> int:
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            return dp(i - 1, j) + dp(i, j - 1)

        return dp(m - 1, n - 1)

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)