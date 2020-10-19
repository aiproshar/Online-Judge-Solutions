//Two pointer method
//Constant space, Linear time complexity
//if two consecutive nums same, increase offset
//else move forward the value based on offset
//Final linear pass to determine length as problem statement 
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0 || nums.size() == 1)
            return nums.size();
        for(int i = 0, offset = 0; i + 1 < nums.size();)
        {
            if(nums[i] == nums[i+1])
            {
                offset++;
                i++;
            }
            else
            {
                nums[i+1 - offset] = nums[i + 1];
                i++;
            }
        }
        int index;
        for(index = 0; index + 1 < nums.size(); index++)
        {
            if(nums[index+1] <= nums[index])
                break;
        }
        return index + 1;
    }
};