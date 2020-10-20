//Naive approach
//94/95 test case passed, last largerst input TLE
//O(n^2) runtime, O(n) memory
//Update if jump count is reduced, forces us to check all possible destination (n * n)
//Needs runtime optimization
class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int>jumps(nums.size(), 1000007);
        jumps[0] = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = 1; j <= nums[i] && i + j < jumps.size(); j++ )
            {
                if(jumps[i + j] > jumps[i] + 1)
                {
                    jumps[i + j] = jumps[i] + 1;
                }
            }
        }
        return jumps[nums.size() - 1];
    }
};
//More optimized solution, same idea but applied carefully
//We start updating from furthest range and decrease to i + 1
//When we fail (no need to update), break the loop
//Because all nodes jumps cost are updated only once
//Reason : we start from least cost nodes and explore others
//thats why only updated once, so when we start from furthest node
//we continue update until already updated
class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int>jumps(nums.size(), 1000007);
        jumps[0] = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = min(i + nums[i], (int)nums.size() - 1); j > i; j--)
            {
                if(jumps[j] > jumps[i] + 1)
                {
                    jumps[j] = jumps[i] + 1;
                }
                else
                    break;
            }
        }
        return jumps[nums.size() - 1];
    }
};
//A different approach - BFS
//Remember that problem, Binary level order traversal ?
//Same strategy, each level means nodes we can explore using that jump
//Each level, we try to explore next levels with 1 jump
//When level ends, we go next level, increase jump :) 
//O(n) runtime complexity, O(1) space complexity
class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0, current_level_max = 0, total_explored = 0; 
        for(int i = 0; i < nums.size() - 1; i++)
        {
            current_level_max = max(current_level_max, i + nums[i]);
            if(i == total_explored)
            {
                total_explored = current_level_max;
                jumps++;
            }
        }
        return jumps;
    }
};