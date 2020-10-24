//Dynamic Programming Solution, bottom up dp, iterative
//Base case : when len <= 3 (j - i + 1 < 4), if front and rear char matches, its palindrome
//Example : aba , aa, bb, c, fff, fzf : all palindrome because front-rear match
//Expand solution space, if i == j it maybe a palindrome, chop off front and rear..
//chars and look for that substr in dp table if its a palindrome or not
//Example :   r********r, this can be a palindrome, we just need to look up 
//in dp table if (*******) is palindrome or not (its computed previously, bottom-up dp)
//O(n^2) time complexity, O(n^2) memory complexity
class Solution {
public:
    string longestPalindrome(string s) {
        int max_size = 0;
        int max_start = 0;
        vector<vector<bool> > dp{s.size(), vector<bool>(s.size(), false)};
        for(int i = s.size() - 1; i >= 0; i--)
        {
            for(int j = i; j < s.size(); j++)
            {
                if(s[i] == s[j])
                {
                    if(j - i < 3 || dp[i + 1][j - 1])
                    {
                        dp[i][j] = true;
                        if(j - i + 1 > max_size)
                        {
                            max_size = j - i + 1;
                            max_start = i;
                        }
                    }
                }
            }
        }
        return s.substr(max_start, max_size);
    }
};
//Other Methods : Longest common substring by reverse string comparison
//Pick location and grow left right as long as palindrome method, constant space complexity
//Everything is described in the solution tab