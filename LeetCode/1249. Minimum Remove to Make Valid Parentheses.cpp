class Solution {
public:
    string minRemoveToMakeValid(string s) {
        
        stack<pair<char, int>>stk;
        
        vector<int>invalid_idx;
        vector<pair<char, int>>vec;

        for(int i = 0; i < s.size(); i++){
            vec.emplace_back(s[i], i);
        }

        for(const auto& [ch, idx] : vec){
            if(ch == '('){
                stk.emplace(ch, idx);
            }
            if(ch == ')'){
                if(!stk.empty() && stk.top().first == '('){
                    stk.pop();
                }else{
                    stk.emplace(ch, idx);
                }
            }
        }

        while(!stk.empty()){
            s.erase(s.begin() + stk.top().second);
            stk.pop();
        }

        return s;
    
    }
};