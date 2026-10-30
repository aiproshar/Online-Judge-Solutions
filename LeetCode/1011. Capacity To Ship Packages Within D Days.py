class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:


        def isPossible(cap: int) -> bool:
            days_r = 1
            current = 0
            for weight in weights:
                current += weight
                if current > cap:
                    days_r += 1
                    current = weight
            return days_r <= days
        # lower bound is the maximum cargo size
        lo = max(weights)
        # upper bound, we ship all in a day
        hi = sum(weights) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if isPossible(mid) is False:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Time Complexity: n * log(sum(n))
# Space Complexity: O(1)