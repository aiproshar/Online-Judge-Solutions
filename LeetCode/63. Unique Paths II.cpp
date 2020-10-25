//Almost same as {62.Unique Paths}
//There are some obstacle, 2D version of staircase with broken stairs
//When Adding the values from previously calculated sub-problem
//check if there is any obstacle and if then skip (multiply by !obstacleGrid[][])
//O(MN) runtime complexity, O(MN) space complexity 
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int> >dp{100, vector<int>(100, 0)};
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        dp[0][0] = 1 * !obstacleGrid[0][0];
        
        for(int i = 1; i < m; i++)
            dp[i][0] = dp[i-1][0]* !obstacleGrid[i][0];
        for(int i = 1; i < n; i++)
            dp[0][i] = dp[0][i-1]* !obstacleGrid[0][i];
            
        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                dp[i][j] = dp[i][j-1] * !obstacleGrid[i][j-1] + dp[i-1][j] * !obstacleGrid[i-1][j];
            }
        }
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
                cout << dp[i][j] << " ";
            cout << endl;
        }
        return dp[m-1][n-1] * !obstacleGrid[m-1][n-1];
    }
};
//Space complexity can be improved to O(n)
//We only need the last row to calculated current row
//Same improvement implementation as {62.Unique Paths}