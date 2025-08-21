class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded;
        encoded.reserve(40000);


        for(int i = 0, temp_len = 0; i < strs.size(); i++){

            temp_len = strs[i].size();
            auto len_str = to_string(temp_len);

            encoded.append(len_str);
            encoded.append(".");
            encoded.append(strs[i]);
        }


        return encoded;
    }

    // Decodes a single string to a list of strings.

    // Chuncked transfer encoding
    // Define size by delimeter, so if the delimeter is present in string we dont give a F
    vector<string> decode(string s) {

        vector<string> strs;

        string currentSize;
        int currentSizeInt;

        for(int i = 0; i < s.size(); ){
            while(s[i] != '.'){
                currentSize.push_back(s[i]);
                i++;
            }

            currentSizeInt = stoi(currentSize);
            i++;
            string tmp;
            while(currentSizeInt--){
                tmp.push_back(s[i]);
                i++;
            }
            strs.push_back(tmp);
            currentSize.clear();
        }

        return strs;

    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));