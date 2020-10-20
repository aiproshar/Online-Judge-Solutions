//Basic dp - optimization problem
//Bottom up iterative
//O(n) time complexity, O(n) space complexity
//Problem statement is not clear for first example, refer to 
//discusion to clearly understand the problem statement
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int>dp(cost.size() + 1, 1000);
        dp[0] = 0;
        dp[1] = 0;
        for(int i = 2; i <= cost.size(); i++)
        {
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]);
        }
        return dp[dp.size() - 1];
    }
};
//Space optimized bottom up
//Almost same as previous solution
//Mod operation to store recently calculated subproblems
//Mod operation logic is kinda hard to describe in text
//We need to found where we recently updated last subproblem
//So we map cost[i-1] with last updated dp[(i-1) % mod]
//We can apply this optimization to "K" steps (O(K) space complexity)
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int>dp(2, 1000);
        dp[0] = 0;
        dp[1] = 0;
        int mod = 2;
        int i;
        for(i = 2; i <= cost.size(); i++)
        {
            dp[i % mod] = min(dp[i % mod] + cost[i-2], dp[(i- 1) % mod] + cost[i-1]);
        }
        return dp[ (i + 1) % mod];
    }
};
//Top down recursive solution
//O(n) time, O(n) {call stack} space complexity
//Little slower than iterative method because call stack overhead
//Iterative - 4ms, recursive - 8 ms
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int>dp(cost.size() + 1, 1000);
        dp[0] = 0;
        dp[1] = 0;
        return recurse(cost.size(), dp, cost);
    }
    int recurse(int n, vector<int>& dp, vector<int>& cost)
    {
        if(n == 0 || n == 1)
            return dp[n];
        if(dp[n] == 1000)
        {
            dp[n] = min(recurse(n-1, dp, cost) + cost[n-1], recurse(n-2, dp, cost) + cost[n-2]);
        }
        return dp[n];
    }
};