

//Basic strings adhoc problem

class Solution {
public:
    string toGoatLatin(string sentence) {

        stringstream ss(sentence);

        vector<string> words;

        //This is important, instead of checking all the vowels in the if block, simplify by comparing agains a set
        // if char == 'a' || char == 'b' || char == 'c' -> unreadable code, this shows you are fkn noob, dont be a noob
        //When its a enum match, drop a hashMap, Set whatever you desire
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

        string word;
        while (ss >> word) {
            cout << word << endl;
            words.emplace_back(word);
        }

        for (auto& word : words) {
            if (vowels.contains(word[0])) {
                word.append("ma");
            } else {
                word.push_back(word[0]);
                word.erase(word.begin());
                word.append("ma");
            }
        }
        string latin;
        latin.reserve(200);
        for (int i = 1; i <= words.size(); i++) {

            latin.append(words[i-1]);
            int cnt = i;
            while(cnt--){
                latin.push_back('a');
            }
            latin.push_back(' ');
        }
        //Omit the very last whitespace
        latin.erase(prev(latin.end()));

        return latin;
    }
};