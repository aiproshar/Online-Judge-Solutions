class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [None] * n
        right_max = [None] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(1, n - 1):
            # corner case, i forgot to remove the height lol
            # But other intuition was ok, we need to left max and right max
            # Our water is hold by the shorter shorter max, so its the amount we can hold here
            current_water = min(left_max[i - 1], right_max[i + 1]) - height[i]
            if current_water > 0:
                total_water += current_water
        return total_water
# Time complexity: O(n) one pass (3 times though)
# Space complexity: O(n) -> storing all the max on both direction