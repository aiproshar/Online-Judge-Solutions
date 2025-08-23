class Solution {

private:
    bool isMatch(const vector<int> &v1, const vector<int> &v2){

        if(v1.size() != v2.size()){
            return false;
        }

        for(int i = 0; i < v1.size(); i++){
            if(v1[i] != v2[i]){
                return false;
            }
        }

        return true;
    }
public:
    bool checkInclusion(string s1, string s2) {


        //s1 should be a substring of s2, that includes both being equal
        //check corner case
        if(s1.size() > s2.size()){
            return false;
        }

        vector<int> count_s1(26, 0);
        vector<int> count_s2(26, 0);

        for(int i = 0; i < s1.size(); i++){
            count_s1[s1[i] - 'a']++;
        }

        for(int i = 0; i < s1.size(); i++){
            count_s2[s2[i] - 'a']++;
        }



        //initial check
        if(isMatch(count_s1, count_s2)){
            return true;
        }

        for(int i = 0, j = s1.size(); j < s2.size(); i++, j++){
            // Remove leftmost character from window
            count_s2[s2[i] - 'a']--;

            // Add new rightmost character to window
            count_s2[s2[j] - 'a']++;

            // Check if current window matches
            if(isMatch(count_s1, count_s2)){
                return true;
            }
        }

        return false;
    }
};