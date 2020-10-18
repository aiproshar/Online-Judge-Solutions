//Just calculate changes and add the profits, we have freedom to buy and sell as many times as we want
//no algorithm, just implementation. Linear scan and add profits
//O(n) time complexity, O(1) space complexity

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector <int> changes;
        changes.push_back(0);
        for(int i = 0 ; i+1 < prices.size() ; ++i)
        {
            changes.push_back(prices[i+1] - prices[i]);
        }
        int ans = 0;
        for(int i = 0; i < changes.size(); i++)
        {
            if(changes[i] > 0)
            {
                ans += changes[i];
            }
        }
        return ans;
    }
};
