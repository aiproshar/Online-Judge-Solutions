
// Brute force solution
// All possible height combination
//  O(n^2), TLE

class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;

        for (int i = 0; i < height.size(); i++) {
            for (int j = i + 1; j < height.size(); j++) {
                int area = (j - i) * min(height[i], height[j]);
                maxArea = max(maxArea, area);
            }
        }

        return maxArea;
    }
};


//Two pointer Approach
//Imagine we start from the left and right most height
//Theres no gain in moving away from the higher bar,
//So lets be greedy, we move away from the smaller bar, hoping we wpuld find bigger bar
//O(n)

class Solution {
public:
    int maxArea(vector<int>& height) {

        int maxArea = 0;

        int lt = 0;
        int rt = height.size() - 1;

        int currentArea = 0;
        while (lt < rt) {
            currentArea = min(height[lt], height[rt]) * (rt - lt);
            maxArea = max(maxArea, currentArea);
            if (height[lt] < height[rt]) {
                lt++;
            } else if (height[lt] > height[rt]) {
                rt--;
            } else {
                lt++;
                rt--;
            }
        }

        return maxArea;
    }
};