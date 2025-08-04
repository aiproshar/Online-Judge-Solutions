//
// Created by arafat on 8/4/25.
//




// This maybe a simple c++ easy problem, but thres more to dig deep
// We can use hashtable, set, or even sorting all sort of fance DSA, but that would hurt the programme, we want cache hit
// So we are using Arrays, with prefill. SO whenever we access count[x], we also get the subsequent values in the l1 cache, hehe.
// This speeds up the process significantly, from like 50+ ns to 1-5 ns, even if we miss the l1, theres l2 and more.
// Sometimes timeComplexity doesn't makes that sense, but l1 cache does. No ones going to beat 1 ns access time.
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> count(26,0);

        for(int i = 0; i < s.size(); i++){
            //Happening in L1 cache
            int idx = s[i] - 'a';
            count[idx]++;
        }

        for(int i = 0; i < t.size(); i++){
            //Happening in L1 cache
            int idx = t[i] - 'a';
            count[idx]--;
        }

        for(auto &it: count){
            //it in L1 cache
            if(it != 0) return false;
        }

        return true;

    }
};