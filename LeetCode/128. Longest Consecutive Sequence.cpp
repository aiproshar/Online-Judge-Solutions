class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.size() == 0) {
            return 0;
        }
        vector<int> cpy = nums;

        sort(cpy.begin(), cpy.end());
        int maxCons = 1;
        int tempCons = 1;
        for (int i = 0; i + 1 < cpy.size(); i++) {
            if (cpy[i + 1] == cpy[i] + 1) {
                tempCons++;

            } else if (cpy[i + 1] == cpy[i]) {
                continue;
            } else {
                maxCons = max(tempCons, maxCons);
                tempCons = 1;
            }
        }

        maxCons = max(tempCons, maxCons);
        return maxCons;
    }
};

// FollowUP

// Implement in linear time complexity
//  Lets try to build consecutive sequence
//  We try to grow left and right
//  We also mark elements which are part of already counted sequence

class Solution {
private:
    int consecSize(const int num, unordered_map<int, bool>& mp) {

        mp[num] = true;
        int ans_size = 1;
        for (int lft = num - 1; mp.find(lft) != mp.end(); lft--) {
            mp[lft] = true;
            ans_size++;
        }

        for (int rht = num + 1; mp.find(rht) != mp.end(); rht++) {
            mp[rht] = true;
            ans_size++;
        }

        return ans_size;
    }

public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, bool> mp;
        mp.reserve(1000);

        for (const auto& it : nums) {
            mp[it] = false;
        }

        int maxSize = 0;
        int currentSize = 0;
        for (const auto& it : mp) {
            if (it.second == false) {
                currentSize = consecSize(it.first, mp);
                maxSize = max(maxSize, currentSize);
            }
        }

        return maxSize;
    }
};
