//Same as maximum subarray problem, just calculate the change of values in a vector
//Ref : maximum-subarray.cpp
//O(n)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> change;
        change.push_back(0);
        for(int i = 0 ; i+1 < prices.size() ; i++)
            change.push_back(prices[i+1] - prices[i]);
        int global_maximum = change[0];
        int current_end_maximum = change[0];
        for(int i = 1 ; i < change.size() ; i++)
        {
            current_end_maximum = max(current_end_maximum + change[i], change[i]);
            if (current_end_maximum > global_maximum)
            {
                global_maximum = current_end_maximum;
            }
        }   
        return global_maximum;      
    }
};