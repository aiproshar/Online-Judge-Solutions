//O(n) time complexity, O(n) space complexity
//Sliding window + hashtable (unordered_map)
//Two pointer(index) method, start and end
//Grow until there's a duplicate, then shrink from start one step
//Update max and when iteration done on whole string max (max is now global max)
class Solution {
public:
    int mxSize = 0;
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, bool> mp;
        for(int start = 0, end = 0; end < s.length();)
        {
            auto it = mp.find(s[end]);
            
            if(it == mp.end())
            {
                mp[s[end++]] = true;
                mxSize = max(mxSize, (int)mp.size());
            }
            else
            {
                mp.erase(s[start++]);
            }
        }
        return mxSize;
    }
};