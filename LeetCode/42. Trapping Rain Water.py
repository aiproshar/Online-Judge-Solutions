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

'''
Followup
Can we do this in constant Space
Two Pointer based solution, hardest part is loop invariant
'''
class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        if n < 3:
            return 0

        left_max = height[0]
        right_max = height[-1]
        left = 0
        right = n - 1
        total = 0
        while left < right:
            # We have left and right, the waters are already at those locations counter
            # We take a step by moving one of those pointers
            # Greedy way, lets move the minimum in a hope to find better maximum pairs in future
            if left_max <= right_max:
                total += max(0, left_max - height[left + 1])
                left_max = max(left_max, height[left + 1])
                left += 1
            else:
                total += max(0, right_max - height[right - 1])
                right_max = max(right_max, height[right - 1])
                right -= 1
        return total

# Time Complexity: O(n)
# Space Complexity: O(1)
