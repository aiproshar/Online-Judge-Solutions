'''
Greedy, how far we can go
The furthest we can go, is it exceeds/reaches the end
Astronomical Questions
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i <= max_reach:
                max_reach = max(max_reach, i + nums[i])
        return  max_reach >= n - 1
# Time Complexity: O(n)
# Space: O(1)