"""
Although part of intervals,
Easy stack problem, modify  top element or append
We need to sort the elements based on start time
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
        return merged
# Time Complexity: n for one pass + nlogn for stdlib sort, so O(nlogn)
# Space Complexity: O(n) if we count output, else O(1)