//Stupid Program IDK maybe took 3-4 hours and +1 hour of debugging
//Thanks GOD VisualStudio has auto exception breakpoint
//Solution : Math + Count Sort: sort accourding to count (bbbbbeeehhac) and then split the first half
//And Merge them with second half b_b_b_b_b_e + e_e_h_h_a_c (merge into blank Spaces)
//Heap Based implementation also possible. Get first two top and construct, if one goes empty pop next most char and continue till end (nlogn)
//If first max has K element, b_b_b_..._b, at least** (k-1 ; total gaps between k elements) elements needed(total rest)
//So solution existence Condition : K + (K -1) > Str.size()
vector<int> count_array(string S) //O(n)
{
    vector<int> char_count;
    for (int i = 0; i < 26; i++)
    {
        char_count.push_back(0);
    }
    for (int i = 0; i < S.size(); i++)
    {
        int temp = int(S[i]);
        temp = temp - int('a');
        char_count[temp]++;
    }
    return char_count;
}
string count_sorted(vector<int> char_count, int str_sz) //O(n) : String Construction Time, counting overhead while constructionconstant
{
    int mx = 0;
    for (auto it = char_count.begin(); it != char_count.end(); it++)
    {
        if (*it > mx)
            mx = *it;
    }
    if ((2 * mx - 1) > str_sz)
    {
        return "";
    }
    else
    {

        string sorted;
        for (int i = 0; i < 26; i++)
        {
            int mx = *max_element(char_count.begin(), char_count.end());
            int mx_idx = max_element(char_count.begin(), char_count.end()) - char_count.begin();
            while (mx--)
                sorted.push_back('a' + mx_idx);
            char_count[mx_idx] = -1;
        }
        return sorted;
    }
}

class Solution
{
public:
    string reorganizeString(string S)
    {
        auto char_count = count_array(S); //O(n)
        string sorted = count_sorted(char_count, S.size()); //O(n)
        if(!sorted.size()) return "";
        string ans;
        ans.resize(S.size()); //O(n)
        int i = 0, j = 0;
        while(i < S.size()) //O(n)
        {
            ans[i] = sorted[j];
            i+=2; j++;
        }
        i = 1;
        while (j != S.size()) 
        {
            ans[i] = sorted[j];
            i+=2; j++;
        }
        return ans;
    }
};
//Total Runtime Complexity : Bunch of stupid O(n), if we get rid of stupid constant its O(n)
