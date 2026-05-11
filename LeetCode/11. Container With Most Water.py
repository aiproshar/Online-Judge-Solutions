# Basic bruteforce
# All possible combination, how much water that can hold
# update global after exploring each local

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        mx = 0
        for i in range(n):
            for j in range(i+1,n):
                curr = min(height[i], height[j]) * (j-i)
                mx = max(mx, curr)
        return mx
# Time Complexity: O(n^2) #TLE on 10^5 input
# Space: O(1)

# Good Problem
# Solved using two pointer
# in every current iteration, update local maxima
# Go in next state in such a way it optimizes
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        mx = 0
        while i < j:
            curr = min(height[i], height[j]) * (j - i)
            mx = max(curr, mx)
            if height[i] < height[j]: # This is the main logic
                                        # The shorter bar is always the bottleneck
                                        # So let's move there hoping we get a bigger bar
                i += 1
            elif height[i] > height[j]: # same on the other side
                j -= 1
            else:
                i += 1
                j -=1
        return mx
# Time Complexity: O(n) -> two pinter one pass
# Space complexity: O(1)
