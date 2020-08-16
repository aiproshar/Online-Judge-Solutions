//Algorith : Kadane's Algorith for O(1) Solution
//Brute Force : O(n^2) solution, Returns global optimum 
//Back to back SWE explanation : https://www.youtube.com/watch?v=2MmGzdiKR9Y
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int last_maximum = 0;
        int global_maximum = nums[0];
        for(int i = 0 ; i < nums.size(); i++)
        {
            int current_end_maximum = max(nums[i], (nums[i] + last_maximum));
            if(current_end_maximum > global_maximum)
            {
                global_maximum = current_end_maximum;
            }
            last_maximum = current_end_maximum;
        }

        return global_maximum;
    }
};