class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        vector<int> combined;
        combined.reserve(nums1.size() + nums2.size());

        int s1 = 0;
        int s2 = 0;

        while (s1 < nums1.size() && s2 < nums2.size()) {

            if (nums1[s1] <= nums2[s2]) {
                combined.emplace_back(nums1[s1]);
                s1++;
            } else {
                combined.emplace_back(nums2[s2]);
                s2++;
            }
        }
        while (s1 < nums1.size()) {
            combined.emplace_back(nums1[s1]);
            s1++;
        }
        while (s2 < nums2.size()) {
            combined.emplace_back(nums2[s2]);
            s2++;
        }
        if(combined.size() % 2){
            int mid_idx = (combined.size()-1)/2;
            return combined[mid_idx];
        }else{
            int mid_idx_right = combined.size() / 2;
            int mid_idx_left = mid_idx_right -1;



            return double(combined[mid_idx_right] + combined[mid_idx_left])/2.00;
        }
    }
};