//My Ever first Hard LeetCode problem, well didn't felt that hard at all
//O(n), so no sorting or greedy approach acceptable
//We can use hashMap for linear time acces without sorting
//Dynamic approach : If 2-3-4-5 are consecutive, we can explore both left and right and return the value
//And mark elements that are grouped, so we dont start searching them again
//C++ doesn't have Python defaultdict, so we use map.find() and compare with map.end() to check key existence (stackover confused me -rep)
//THe is something called disjoint union set or something. IDK what is that maybe similar or i accidentally implemented it who knows !
//Similarity with Kadane's algorithm, looks greedy but also dp behaviour
//The Beauty of OOP and reusable code BABY!
class Helper
{
public:
    static int extend_cont(int num, map<int,bool> &is_grouped, string increment_direction)
    {
        int ans = 1;
        while(1)
        {
            if(increment_direction == "left") num--;
            if(increment_direction == "right") num++;
            auto it = is_grouped.find(num);
            if(it == is_grouped.end()) return ans; //Value doesn't exist in list
            if(!it->second)
            {
                it->second = true;
                ans++;
            }
            else 
            {
                return ans;
            }  
        }
    }
};

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        map<int, bool> is_grouped;                  //Initialing grouped
        for(int i = 0; i < nums.size(); i++)
        {
            is_grouped[nums[i]] = false;
        }
        int ans = 0;
        for(auto it = is_grouped.begin(); it != is_grouped.end(); it++)
        {
            if(it->second == false) //not grouped yet
            {
                int inc_left = Helper::extend_cont(it->first, is_grouped, "left");
                int inc_right = Helper::extend_cont(it->first, is_grouped, "right");
                if (inc_left + inc_right - 1 > ans) ans = inc_right + inc_left -1;   //if we start from 2, we grow both left and right, counting 2 twice; thats why -1
            }
        }
        return ans;
    }
};