//Top down dp
//Recursive + memoization
//O(n) time, O(n) space
//Back to Back SWE explanation : https://www.youtube.com/watch?v=NFJ3m9a1oJQ
class Solution {
public:
    int climbStairs(int n) {
        int dp[50];
        memset(dp, -1, sizeof(dp));
        dp[0] = 1;
        dp[1] = 1;
        return fib(n, dp);
    }
    int fib(int n, int dp[])
    {
        if(dp[n] != -1)
            return dp[n];
        dp[n] = fib(n-1, dp) + fib(n-2, dp);
        return dp[n];
    }
};

//Follow up
//Optimized iterative, bottom up dp
//Constant space
//Some implementaton tricks, return the value from temp that is recently updated
class Solution {
public:
    int climbStairs(int n) {
        bool bool_idx = 0;
        int temp_0 = 1;
        int temp_1 = 1;
        for(int i = 2 ; i <= n; i++)
        {
            if(!bool_idx)
            {
                temp_0 = temp_0 + temp_1;
                bool_idx = 1;
            }
            else
            {
                temp_1 = temp_0 + temp_1;
                bool_idx = 0;
            }           
        }
        if(bool_idx)
            return temp_0;
        else
            return temp_1;
    }
};
