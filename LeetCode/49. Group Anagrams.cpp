//Just create a unoque id for each anagram, so we can use that as key
// So lets sort the strings, a u_id for each anagram, and use it as key
//Use another vector as value, and keep pushing all the matched anagrams


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > ags;
        ags.reserve(10000);

        for(auto &it: strs){
            auto tmp_str = it;
            sort(tmp_str.begin(), tmp_str.end());
            ags[tmp_str].emplace_back(it);
        }


        //Lets iterate over string vectors in the map -> create a vector of strings
        vector<vector<string>> ans;
        for(auto const &it: ags){
            ans.emplace_back(it.second);
        }
        return ans;

    }
};

//Time complexity: O(n) ammortized