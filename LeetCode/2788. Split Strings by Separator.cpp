
// This is more like a generic solution, split string based on other strings or char (in this case)

class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> strs;

        for (auto str: words) {

            // This is more like a two pointer approach, lets find the first matching start, spos
            //Also try to find the next matching position

            unsigned long spos = 0;
            unsigned long currentPos =  str.find(separator, spos);
            if (currentPos == -1) {
                //means no substr match
                strs.push_back(str);
                continue;
            }
            while (currentPos != -1) {
                auto  _substr = str.substr(spos, currentPos - spos);
                if (!_substr.empty()) {
                    strs.push_back(_substr);
                }
                spos = currentPos + 1; // separator.size() when we are using string to split another string. YaY
                //Next place which is just after the delim match end position
                currentPos =  str.find(separator, spos);
            }
            if(spos != str.size()){
                strs.push_back(str.substr(spos));
            }
        }

        return strs;
    }
};
