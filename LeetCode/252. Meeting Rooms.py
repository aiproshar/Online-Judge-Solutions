"""
Basic Interval Problem
Sort and check next.start before current.end or not
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
# Time Complexity: O(nlogn) + O(n) -> Sort stdliv
# Space Complexity: O(1) or O(n) because we doing sort in place