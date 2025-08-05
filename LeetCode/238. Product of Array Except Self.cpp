
// Took a bit time, because of how to handle prefix and suffix and index
// Initially though pfx[i] will be pfx[0]*pfx[1]*...pfx[i-1], actual one
// This made the implementation hard, bugged, hours wasted, but it made ans[i] = pfx[i] + sfx[i] -> easy
// Then pfx[i] means upto p[i], it includes p
//so now to calcualte ans[i], we need to +/- to pfx and sfx from i
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> pfx(nums.size(), 1);
        vector<int> sfx(nums.size(), 1);

        pfx[0] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            pfx[i] = pfx[i - 1] * nums[i];
        }

        sfx[nums.size() - 1] = nums[nums.size() - 1];

        for (int i = nums.size() - 2; i >= 0; i--) {
            sfx[i] = sfx[i + 1] * nums[i];
        }

        vector<int> ans(nums.size(), 1);
        ans[0] = sfx[1];
        ans[nums.size() - 1] = pfx[nums.size() - 2];

        for (int i = 1; i + 1 < nums.size(); i++) {
            ans[i] = pfx[i - 1] * sfx[i + 1];
        }

        return ans;
    }
};
// O(n) jeez