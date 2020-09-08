//Basic Binary Search on sorted array
//Returns true upon first expected value encounter, there may be more than one but the algo will return immediately 
//Avoided (lo + hi) / 2 to avoid accidental overflow
//Recursive: Easier to understand and implement, but slower (stack push and poping) 
//But in practice, imagine a huge array (10 ^ 30)... only 100 max depth recursion //No chance of stack overflow, fewer lines of code
//Errichto Theory + Implementation : https://www.youtube.com/watch?v=GU7DpgHINWQ 

int recursive_bisearch(vector<int>& nums, int lo, int hi, int target);
int iterative_bisearch(vector<int>& nums, int target);
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return recursive_bisearch(nums, 0, nums.size()-1, target);
        //return iterative_bisearch(nums, 0, nums.size()-1, target);
    }
};


int recursive_bisearch(vector<int>& nums, int lo, int hi, int target)
{
    if(lo > hi) return -1;
    int mid = lo + (hi - lo)/2;
    if(target == nums[mid]) return mid;
    if(target > nums[mid]) return recursive_bisearch(nums, mid+1, hi, target);
    if(target < nums[mid]) return recursive_bisearch(nums, lo, mid-1, target);
    return -1;
}

int iterative_bisearch(vector<int>& nums, int target)
{
    int lo = 0;
    int hi = nums.size() - 1;
    while(lo <= hi)
    {
        int mid = lo + (hi - lo)/2;
        if (target > nums[mid])
        {
            lo = mid+1;
        }  
        else if (target < nums[mid])
        {
            hi = mid - 1;
        }
        if (target == nums[mid]) return mid;
    }
    return -1;
}