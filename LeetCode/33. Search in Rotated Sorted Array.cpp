//Same as https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
//We need to find pivot first
//Then split the array into two non-decreasing array
//Then search on them using biSearch to find our guy


class Solution {
private:
    int findMidPoint(const vector<int>& nums) const{


        int lo = 0;
        int hi = nums.size() - 1;

        while(hi - lo > 1){
            int mid = (lo+hi) / 2;

            if(nums[mid] < nums[lo]){
                hi = mid;
            }else{
                lo = mid;
            }
        }
        return hi;
    }

    int biSearch( const vector<int>& nums, int lo, int hi, int value) const{
        
        while(lo <= hi){
            int mid = (lo + hi) / 2;
            if(nums[mid] == value){
                return mid;
            }
            if(value > nums[mid]){
                lo = mid+1;
            }else{
                hi = mid - 1;
            }
        }
        return -1;
    }
public:
    int search(vector<int>& nums, int target) {

        auto pivot = findMidPoint(nums);

        if(target == nums[pivot]){
            return pivot;
        }
        if(target > nums[pivot] && target <= nums[nums.size() - 1]){
            return biSearch(nums, pivot, nums.size()-1, target);
        }else{
            return biSearch(nums, 0, pivot - 1, target);
        }

    }
};