


class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> strs;

        for (auto str: words) {
            unsigned long spos = 0;
            unsigned long currentPos =  str.find(separator, spos);
            if (currentPos == -1) {
                strs.push_back(str);
                continue;
            }
            while (currentPos != -1) {
                auto  _substr = str.substr(spos, currentPos - spos);
                if (!_substr.empty()) {
                    strs.push_back(_substr);
                }
                spos = currentPos + 1;
                currentPos =  str.find(separator, spos);
            }
            if(spos != str.size()){
                strs.push_back(str.substr(spos));
            }
        }

        return strs;
    }
};
