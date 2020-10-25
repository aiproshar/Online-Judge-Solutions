//Basic Iterative dp
//Same as {70. Climbing Stairs}, this is just 2D version
//Initialize base cases in dp table;
//O(mn) time complexity, O(mn) space complexity
class Solution {
public:
    int uniquePaths(int m, int n) {
        int dp[100][100];
        memset(dp, 0, sizeof(dp));

        for(int i = 0; i < m; i++)
            dp[i][0] = 1;
        for(int i = 0; i < n; i++)
            dp[0][i] = 1;
        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
//Space can be optimized further to O(N), not O(M)
//M->No of rows and N->size of each row and vice versa
//We only need the last row to iterate through 
//the sub-problems of current row
//swap the values or use flag variable(more efficeint) to 
//preserve states (which row we modify now ?)
class Solution {
public:
    int uniquePaths(int m, int n) {
        int dp[2][100];
        memset(dp, 0, sizeof(dp));

        for(int i = 0; i < 2; i++)
            dp[i][0] = 1;
        for(int i = 0; i < n; i++)
            dp[0][i] = 1;
        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                dp[1][j] = dp[0][j] + dp[1][j-1];
            }
            swap(dp[0], dp[1]);
        }
        return dp[0][n-1];
    }
};