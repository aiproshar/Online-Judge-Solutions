# Simple Solution
# We can rotate clockwise and counter to reach from a to b, we greedily pick best way
class Solution:
    def minRotations(self, s: str) -> int:
        total = 0
        prev = 0
        for ch in s:
            num = int(ch)
            total += (min((10 - num + prev), abs(num - prev), (10 - prev + num)))
            prev = num
        return total

# Time Complexity: O(n)
# Space: O(1)