//Map Based solition
//abs(number) is our key
//value is positive_count and negative_count
//then we iterate, as this is sorted map, we iterate from low to high (assuming we have comparator)
//O(n) time and space complexity
class Solutions {
public:
    vector<int> sortByAbsoluteValue(vector<int>& nums) {
        map<int,pair<int,int>>mp;

        for(const auto& num:nums){
            auto idx = abs(num);
            if(num >= 0){
                mp[idx].first++;
            }else{
                mp[idx].second++;
            }
        }
        vector<int> ans;
        for(const auto& it:mp){
            int pos_count = it.second.first;
            int neg_count = it.second.second;
            while(neg_count--){
                ans.push_back(it.first*-1);
            }
            while(pos_count--){
                ans.push_back(it.first);
            }
        }

        return ans;
    }
};