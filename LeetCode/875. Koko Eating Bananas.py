# Bound based binary search
#

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_time(speed: int) -> int:
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            return time
        max_pile = max(piles)

        lo = 1
        hi = max_pile
        # This is lower bound bi_search problem
        # We want the smallest speed that satisfies
        # Assume speed 7 takes 4 hours, speed 6 can also take 4 hours, that's a bound problem

        while lo < hi:
            mid = (lo + hi) // 2
            current_time = total_time(mid)
            if h >= current_time:
                hi = mid
            if h < current_time:
                lo = mid + 1
        return lo
# time complexity: O(loN)
# Space complexity: O(1)