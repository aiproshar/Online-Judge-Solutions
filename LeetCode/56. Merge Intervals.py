"""
Although part of intervals,
Easy stack problem, modify  top element or append
We need to sort the elements based on start time
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], interval[1])
                else:
                    res.append(interval)
        return res
# Time Complexity: n for one pass + nlogn for stdlib sort, so O(nlogn)
# Space Complexity: O(n) if we count output, else O(1)