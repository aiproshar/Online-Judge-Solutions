//innovative solution

//We take mid point, scope out the sorted half
//The pivot point is present in unsorted array
//5,6,7,8,2,3 -> 2 is the pivot point
//We want to get back to last invalid sub array (8:2 -> in this case)
//Then just print the later of the 2 sized subarray
//make sure dont use mid+1, by doing that we can miss out pivot values
class Solution {
public:
    int findMin(vector<int>& nums) {
        
        if(nums[0] < nums[nums.size() - 1]){
            return nums[0];
        }
        int lo, hi;
        for(lo = 0, hi = nums.size() - 1; hi - lo > 1; ){
            
            int mid = (lo + hi) / 2;
            if(nums[lo] < nums[mid]){
                lo = mid ;
            }else{
                hi = mid;
            }
        }


        return nums[hi];
    }
};