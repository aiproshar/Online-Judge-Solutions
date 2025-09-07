//First thing in mind
//Sort and go to size() - K
//time: O(nlog n), space: O(n)

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        sort(nums.begin(), nums.end());

        return nums[nums.size() - k];
    }
};

//option 2
//min heap
//time: O(nlgk)
//Space: O(k)
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int, vector<int>, greater<int>>pq;

        for(const auto& num: nums){
            pq.push(num);

            if(pq.size() > k){
                pq.pop();
            }
        }

        return pq.top();

    }
};

//Count sort
//Its always linear
//O(N) where N -> range of n {-10^4, +10^4} Fcked
//Time Complexity: Linear + (table doubling OOPS)
//Space complexity: N -> range of nums[i]
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        unordered_map<int,int>mp;
        //mp.reserve(1000);

        for(const auto& num:nums){
            mp[num]++;
        }

        for(int i = 10000; i >= -10000; i--){
            k-=mp[i];
            if(k <= 0){
                return i;
            }
        }
        return -1;
    }
};