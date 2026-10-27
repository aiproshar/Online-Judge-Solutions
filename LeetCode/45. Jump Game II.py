"""
Classic brute force solution

If we at i, what index we can reach, its i + 1 to i + nums[i] right
So we update the dp table,in each index we try to update all the reachable from there, with new mim
Bottom up dp
"""

class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = defaultdict(lambda: math.inf)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i+1, i+nums[i]+1):
                dp[j] = min(dp[i] +1, dp[j])
        return dp[len(nums) - 1]

# Time Complexity: O(n.k) where k is avg jump length, worst case O(n^2) -> we can jump to end from every node
# Space Complexity: O(n) 1D dp table


'''
True DP, we do backward to update the dp table
As soon as we reach a cell which was previously updated, we break. Because previous means less jumps
And this small optimization drastically reduced our TC
We can do more optimization here, nums[i] + K can go out of bound, we setting dp values for out of state space
That will guranteed what we do only O(n) operations
'''
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n
        # dp[i] -> min jump to reach ith location
        # base case
        dp[0] = 0
        for i in range(n):
            # overreach corner case
            reach = min(n - 1, i + nums[i])
            while reach > i:
                if dp[reach] > dp[i] + 1:
                    dp[reach] = dp[i] + 1
                    reach -= 1
                else:
                    break
        return dp[n-1]
# Time Complexity: O(n+k). How ? We touching previously updated cells at most n times. Becase of early break
# K is our avg jump length
# Space: O(n)

"""
A different approach - BFS
Remember that problem, Binary level order traversal?
Same strategy, each level means nodes we can explore using that jump
Each level, we try to explore next levels with 1 jump
When level ends, we go next level, increase jump :)
O(n) runtime complexity, O(1) space complexity
"""
class Solution:
    def jump(self, nums: List[int]) -> int:

        cur_max = 0
        fut_max = 0
        jumps = 0
        for i in range(len(nums) - 1):
            fut_max = max(fut_max, i + nums[i])
            if i == cur_max:
                cur_max = fut_max
                jumps += 1
        return jumps
