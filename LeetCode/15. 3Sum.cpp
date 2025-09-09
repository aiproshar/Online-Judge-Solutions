//Typical brute force approach
//O(n^3)
//We do check exact same number for exact position, and skip those

class Solution {
public:

    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> ans;

        unordered_map< string, bool>  mp;

        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++){
            if(i > 0 && (nums[i] == nums[i-1]))
                continue;
            for(int j = i+1; j < nums.size(); j++){
                if(j > i+1 && nums[j-1] == nums[j])continue;
                for(int k = j+1; k < nums.size(); k++){
                    //if(k > j+1 && nums[k-1] == nums[k])continue;
                    if (nums[i] + nums[j] + nums[k] == 0){
                        ans.push_back({nums[i],nums[j],nums[k]});
                        break; // Yes, i and j are same here,so if we match a K then we break the loop, future K matches will be duplicate anyways
                        //You can also use **if(k > j+1 && nums[k-1] == nums[k])continue;** but this one is better, we do early termination YaY
                    }
                }
            }
        }
        return ans;
    }
};



class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) { //nums = {-100, ->100    -1,-1,0,1,4,4}

        vector<vector<int>> ans;

        unordered_map<string, bool> mp;

        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && (nums[i] == nums[i - 1]))
                continue;
            auto target = -1 * nums[i];
            for (int lo = i + 1, hi = nums.size() - 1; lo < hi; ) {
                if (lo > i + 1 && nums[lo] == nums[lo - 1]){
                    lo++;
                    continue;
                }
                if ((nums[lo] + nums[hi]) == target) {
                    ans.push_back({nums[lo], nums[hi], nums[i]});
                    lo++;
                    hi--;
                }else if ((nums[lo] + nums[hi]) > target){
                    hi--;
                }else{
                    lo++;
                }
            }
        }
        return ans;
    }
};