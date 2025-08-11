

//Using unordered Map
//Ascii string char ---> eqv int: as key
//Count as value
 Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map<int, int> mp;
        for (int i = 0; i < s.size(); i++) {
            mp[s[i]] = 0;
        }

        int currentSize = 0;
        int maxSize = 0;

        for (int i = 0, j = 0; j < s.size(); j++) {
            mp[s[j]]++;
            currentSize++;
            // We insert first and then figure out if we are fkd
            //If so then we start removing elements until we good
            if (mp[s[j]] > 1) {
                maxSize = max(maxSize, currentSize - 1);
                while (mp[s[j]] > 1) {
                    mp[s[i]]--;
                    currentSize--;
                    i++;
                }
            }
        }

        maxSize = max(maxSize, currentSize);

        return maxSize;
    }
};

//Using unordered_set

class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_set<char> st;
        st.reserve(1000);

        int mx = 0;

        for(int i =0, j= 0; j < s.size(); j++){
        // We are using set, so no duplicate
        // We must check before inserting, cause we wont be able to tell later
            if(st.find(s[j]) != st.end()){
                mx = max(mx, (int)st.size());
                while(s[i] != s[j]){
                    st.erase(s[i]);
                    i++;
                }
                i++;
            }else{
                st.insert(s[j]);
            }
        }
        mx = max(mx, (int)st.size());
        return mx;
    }
};