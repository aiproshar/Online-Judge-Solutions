//Naive Approach, Bottom Up recursive
//Brute Force, Exponential Complexity O(2^n)
class Solution {
    string text1, text2;
public:
    int longestCommonSubsequence(string text1, string text2) {
        Solution::text1 = text1;
        Solution::text2 = text2;
        return lcs_recursive(text1.length() - 1, text2.length() - 1);
    }
    int lcs_recursive(int l1, int l2)
    {
        if(l1 < 0 || l2 < 0)
            return 0;
        if(text1[l1] == text2[l2])
        {
            return 1 + lcs_recursive(l1 - 1, l2 - 1);
        }
        else
        {
            return max(lcs_recursive(l1 - 1, l2), lcs_recursive(l1, l2 - 1));
        }
    }
};
//Recursive Dp - Top down dp, Bottom up recursion
//Subproblem memoization - form last index (last index of our current strings)
//Each state has two states, so exponential growth but we have subproblem overlap
// "abcde" , "wxyz" will sure have a common subproblem ("abcd", "wxy") in 1 level down states, subproblem 
//overlap also grows exponentially (2 common subproblem -> 4 commom subproblem-> 8-> 16......)
//Using map{RBT} (O(lgN)) also gets TLE, so vector is only option
//Cannot use unordered_map(no hash function for pair :( ))
//Errichto Description : https://www.youtube.com/watch?v=KJWAQVmuFW0 
class Solution {
    vector< vector<int> > v{1001, vector<int>(1001, -1)};
    string text1, text2;
public:
    int longestCommonSubsequence(string text1, string text2) {
        Solution::text1 = text1;
        Solution::text2 = text2;
        return lcs_recursive(text1.length() - 1, text2.length() - 1);
    }
    int lcs_recursive(int l1, int l2)
    {
        if(l1 < 0 || l2 < 0)
            return 0;
        if(v[l1][l2] != -1)
            return v[l1][l2];
        if(text1[l1] == text2[l2])
        {
            return v[l1][l2] = 1 + lcs_recursive(l1 - 1, l2 - 1);
        }
        else
        {
            return v[l1][l2] = max(lcs_recursive(l1 - 1, l2), lcs_recursive(l1, l2 - 1));
        }
    }
};
//2D dp table, iterative bottom up dp
//Similarity with minimum edit distance{72. Edit Distance}
//Base Case : empty string column in dp table initialized by 0
//When char matches, go (i-1, j-1), chop off last char from both string
//WHen no match, pick max from {(i,j-1), (i-1,j)} -> similar what recursion does in else block
//Back to Back SWE explanation: https://www.youtube.com/watch?v=ASoaQq66foQ
//Back to Back SWE, Hats off brother. You are the best!
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int> > dp{text1.size() + 1, vector<int>(text2.size() + 1, 0)};
        //Index zero for empty string (base case), so we offset string access value by 1
        for(int i = 1; i <= text1.size(); i++)
        {
            for(int j = 1; j <= text2.size(); j++)
            {
                if(text1[i-1] == text2[j-1])
                {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else
                {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[text1.size()][text2.size()];
    }
};