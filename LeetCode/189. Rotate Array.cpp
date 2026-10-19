//Extra Space Method
//K % size() ; avoiding extra full cycle rotation
//Just extend the array (2x), if we rotate top k elements should be added in the front
//so remove size() - K elements from to
//pop until matches initial size
//O(n) for copy + O(n) for removing front and back elements

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int initial_size = nums.size();
        k = k % nums.size();
        auto nums_ext = nums;
        nums.insert(nums.end(), nums_ext.begin(), nums_ext.end());
        nums.erase(nums.begin(), nums.begin() + (initial_size - k));
        while(nums.size() != initial_size)
        {
            nums.pop_back();
        }
    }
};

//Inplace O(1) solution by leetcode using reverse
//If you come up with O(n) solution, interviewer may ask to optimize space complexity
//Intuition :(output to input construction) 5-6-7-1-2-3-4 -> 5-6-7 || 1-2-3-4 ->(reversing in kth point) : 7-6-5-4-3-2-1
//so solution : 1-2-3-4-5-6-7 ->(rev) 7-6-5-4-3-2-1 ->Divide 7-6-5 || 4-3-2-1 ->(reverse in kth position): 5-6-7-1-2-3-4
//O(n) time complexity,O(1) space complexity
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k = k % nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin() + k);
        reverse(nums.begin()+k, nums.end());
    }

};

//4 ms, first solution took 20ms.