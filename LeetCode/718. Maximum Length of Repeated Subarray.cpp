//bottom up dp, 2d dp table
//If we have a char match, look for next char in both string {dp table, subproblem overlap}
//dp table has partial similarity with longest common subsequence problem
//Padded with '0' so base subproblem(out of bound) is zero
//using array insted of dp improves runtime(140 ms vs 330)
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int dp[A.size()+1][B.size()+1];
        memset(dp, 0, sizeof(dp));
        int max_len = 0;
        for(int i = A.size() - 1; i >=  0; i--)
        {
            for(int j = B.size() - 1; j >= 0; j--)
            {
                if(A[i] == B[j])
                {
                    dp[i][j] = 1 + dp[i+1][j+1];
                    if(dp[i][j] > max_len)
                        max_len = dp[i][j];
                }
            }
        }
        return max_len;
    }
};