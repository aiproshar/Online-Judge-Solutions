class Solution {
public:
    // First Solution, Brute force the hell out
    //  All possible valid combination (sellDay is later then buyDay)
    //  compare localMax, return GlobalMax
    int maxProfit(vector<int>& prices) {

        int mx = 0;
        for (int i = 0; i < prices.size(); i++) {
            for (int j = i + 1; j < prices.size(); j++) {
                mx = max(mx, prices[j] - prices[i]);
            }
        }

        return mx;
    }

    // FollowUp
    // O(n) based approach
    // Break to subproblem and extend scope
    // What is the possible maxSum in 0 - ith index ?
    // Its the max of previous (i-1) and value in i
    // We calculate all the local maximas
    // Also compare to previous best local maxima to get globalMaxia in the end
    int maxProfit(vector<int>& prices) {

        int localMax = 0;

        vector<int> profit(prices.size(), 0);

        for (int i = 1; i < prices.size(); i++) {
            profit[i] = prices[i] - prices[i - 1];
        }

        int globalMax = 0;
        for (int i = 1; i < profit.size(); i++) {
            localMax = max(localMax + profit[i], profit[i]);
            globalMax = max(localMax, globalMax);
        }
        return globalMax;
    }
};