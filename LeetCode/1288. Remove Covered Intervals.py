'''
Sweep Line, with a bit trick in sorting
If we have multiple intervals starts at same, we sort based on reverse end, means longest interval comes first

The rest is sweep line, if totally consumed, skip, else take the new one increaee counter
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))
        current = intervals[0]
        res = 1
        for start, end in intervals[1:]:
            if start <= current[1] and end <= current[1]:
                continue
            else:
                current = [start, end]
                res += 1
        return res

# Time Complexity: O(nlogn)
# Space: O(1), additional space for build in sort is upto O(n)