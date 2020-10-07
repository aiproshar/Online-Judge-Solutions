//Recursion
//Time Complexity O(2^n), memory O(n) {max call stack size}
class Solution {
public:
    int fib(int N) {
        if(!N)
            return 0;
        if(N == 1 || N == 2)
            return 1;
        return fib(N-1) + fib(N-2);
    }
};
//recursive + memoization
//O(n) time complexity, O(n) space complexity
class Solution {
    int dp[31];
public:
    Solution()
    {
        memset(dp, -1, sizeof(dp));
        dp[0] = 0;
        dp[1] = 1;
    }
    int fib(int N) {
        if(dp[N] == -1)
        {
            dp[N] = fib(N-1) + fib(N-2);
            return dp[N];
        }
        return dp[N];
    }
};