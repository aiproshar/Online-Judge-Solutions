//Basic Backtracking Combination Generation
//More input string can have duplicate items
//Sort and explore depth. If next == current just find the next non-similar element(sorted)
//For permutation start from 0 for all possible states
//For combination if we are in i-th character state start fom next (call recursion with initial point i+1)
//Choices, Constrains, Goals :) Back to Back SWE: https://www.youtube.com/watch?v=Zq4upTEaQyM 

#define READ freopen("in.txt", "r", stdin)
#define WRITE freopen("out.txt", "w", stdout)
#include <bits/stdc++.h>
using namespace std;

int depth;
vector<bool> taken(40, false);
vector<char> ans;
string str;
void combination(int idx, int start)
{
    if (idx == depth)
    {
        for (int i = 0; i < ans.size(); i++)
        {
            cout << ans[i];
        }
        cout << endl;
        return;
    }
    for (int i = start; i < str.size(); i++)
    {
        if (!taken[i])
        {
            taken[i] = true;
            ans.push_back(str[i]);
            combination(idx + 1, i + 1); //permutation(id+1, 0) ->start from first possible state
            ans.pop_back();
            taken[i] = false;
            while(str[i] == str[i+1]) i++; //Duplicate element guard, if no duplicate this wont hurt anyway
        }
    }
}

int main()
{
    //READ;
    //WRITE;
    while (cin >> str >> depth)
    {
        sort(str.begin(), str.end());
        combination(0, 0);
        ans.clear();
        fill(taken.begin(), taken.end(), false);


    }
}