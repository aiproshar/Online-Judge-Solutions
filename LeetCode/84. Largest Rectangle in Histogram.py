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



# This was really hard, and an extreme use of monotonic stack
# Monotonically increasing stack, we pop when we find a short bar
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            if not stack or height >= stack[-1][1]:
                stack.append((idx, height))
            else:
                last_idx = None
                while stack and height < stack[-1][1]:
                    last_idx = stack[-1][0]
                    current_area = stack[-1][1] * (idx - stack[-1][0])
                    max_area = max(max_area, current_area)
                    stack.pop()
                # This is edge case, we must extend our bar as far back behind possible, we dont need to start from current idx
                stack.append((last_idx, height))
        n = len(heights)
        # Another corner case,we was having element which was increasing, and the iteration end, means we hit the right wall
        while stack:
            current_area = stack[-1][1] * (n - stack[-1][0])
            max_area = max(max_area, current_area)
            stack.pop()
        return max_area
