//Although seems easy, not easy at all, linear time complexity not allowed
//You have to find both first and last element with binary search (good luck traversing the array with O(n))
//null and single element vectors allowed, handeled by hard code
//Other Edge Case : Whole array Target
//Two different fuction for start and end postion finding (Messed up while generalizing)
//Its Always mid implementation _________--------________ imagine the high section is your target(s), if mid hits there 
//you want to relocate start if you willing to find end(start may have already crossed start point but we must be carefull swapping end)
//same goes for finding end, move start pointer (vice versa)
//Errichto Explanation : https://www.youtube.com/watch?v=dVXy6hmE_0U
//Nick White Explanation : https://www.youtube.com/watch?v=bU-q1OJ0KWw
//** Make Code redable and easy to understand, dont be a jerk by writing 10-20 lines of code
//Yeah i knowtwo search functions have 1 line of difference, i am just lazy to write single function

class Search
{
private:
    /* data */
public:
    int Modified_bi_search_start(vector<int> &arr, int s, int e, int val)
    {
        int mid = ((s + e) / 2.0);
        if (e == s + 1)
        {
            if (arr[s] == val)
                return s;
            if (arr[e] == val)
                return e;
            return -1;
        }
        if (arr[mid] == val)
            return Modified_bi_search_start(arr, s, mid, val);
        if (arr[mid] > val)
            return Modified_bi_search_start(arr, s, mid, val);
        if (arr[mid] < val)
            return Modified_bi_search_start(arr, mid, e, val);
        return -1;
    }

    int Modified_bi_search_end(vector<int> &arr, int s, int e, int val)
    {
        int mid = ((s + e) / 2.0);
        if (e == s + 1)
        {
            if (arr[e] == val)
                return e;
            if (arr[s] == val)
                return s;
            return -1;
        }
        if (arr[mid] == val)
            return Modified_bi_search_end(arr, mid, e, val);
        if (arr[mid] > val)
            return Modified_bi_search_end(arr, s, mid, val);
        if (arr[mid] < val)
            return Modified_bi_search_end(arr, mid, e, val);
        return -1;
    }
};

class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        Search s;
        if (!nums.size())
        {
            vector<int> ans;
            ans.push_back(-1);
            ans.push_back(-1);
            return ans;
        }
        if (nums.size() == 1)
        {
            if (nums[0] == target)
            {
                vector<int> ans;
                ans.push_back(0);
                ans.push_back(0);
                return ans;
            }
            else
            {
                vector<int> ans;
                ans.push_back(-1);
                ans.push_back(-1);
                return ans;
            }
        }
        int start = s.Modified_bi_search_start(nums, 0, nums.size() - 1, target);
        int end = s.Modified_bi_search_end(nums, 0, nums.size() - 1, target);
        vector<int> ans;
        ans.push_back(start);
        ans.push_back(end);
        return ans;
    }
};