class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int>dict;

        for(const auto& word : words){
            dict[word]++;
        }
        auto lambda = [](const auto& ob1, const auto& ob2 ){
            if(ob1.second == ob2.second){
                return ob1.first < ob2.first;
            }
            return ob1.second > ob2.second;
        };
        
        vector<pair<string, int>>vec;
        vec.reserve(dict.size());

        for(const auto& [key, value]:dict){
            vec.emplace_back(key,value);
        }
        sort(vec.begin(), vec.end(), lambda);

        vector<string>most_frequent;
        most_frequent.reserve(k);

        for(int i = 0; i < k; i++){
            most_frequent.emplace_back(vec[i].first);
        }

        return most_frequent;
    }
};