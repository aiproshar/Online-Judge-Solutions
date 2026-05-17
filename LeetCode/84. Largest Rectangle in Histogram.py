# Brute force approach
# Generate all possible start/end point and track the min height, which is bottleneck
# Calculate Are, vertical (min height) * horizontal (distance)
# TLE
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mx_area = 0
        for i in range(n):
            min_height = math.inf
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                mx_area = max(mx_area, area)
        return mx_area
# Time complexity: O(n^2)
# Space complexity: O(n)