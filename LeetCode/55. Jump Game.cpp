//Trivial solution
//Bottom up
//Memoization to skip the nodes we cannot reach
//74/75 test case passed, last case (maximum input) TLE
//Further optimization TLE too (TLE upon dp[size - 1] halt)
class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<bool> dp(nums.size(), false);
        dp[0] = true;
        for(int i = 0; i < dp.size(); i++)
        {
            if(!dp[i])
                continue;
            else
            {
                for(int range = 1; range <= nums[i] && i + range < nums.size(); range++)
                {
                    if(!dp[i + range])
                    {
                        dp[i + range] = true;
                    }
                }
            }
        }
        return dp[dp.size() - 1];
    }
};
//Greedy approach
//Similarity with Kadane's algorithm {121.Best time to buy and sell stock}
//Optimal in local, increase local space
//When we are in global, now we have solution for global space
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reachable_index = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(i > reachable_index)
                break;
            int current_index = min(i + nums[i], (int)nums.size() - 1);
            reachable_index = current_index > reachable_index ? current_index : reachable_index;
        }
        if(reachable_index == nums.size() - 1)
            return true;
        else
            return false;
    }
};