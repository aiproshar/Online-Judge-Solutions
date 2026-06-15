
"""
Non-overlapping Intervals (LeetCode 435)

Sort by start position. Walk through pairs: if the current interval starts
before the previous one ends, they overlap and we must remove one.
Remove the one that ends later — keeping the shorter tail leaves more
room for future intervals and minimizes total removals.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        previous = intervals[0]
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < previous[1]:
                remove += 1
                if  intervals[i][1] < previous[1]:
                    previous = intervals[i]
            else:
                previous = intervals[i]
        return remove

# Time Complexity: nlogn + n -> O(nlogn)
# Space Complexity: O(n) or can be O(1) because we sorted inplace, talk with interviewer


"""
A unique problems on intervals
This is editorial approach, we sort based on end timer
SO we process earliest meeting first
So whenever a collision, we must move one, the question is which one
The more someone collides with other the endtime will be larger and they will come last

So, if current one starts before previous end, there's a collision. We remove current one
If not our new collision free interval becomes current
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        previous = intervals[0]
        remove = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < previous[1]:
                remove += 1
                if  intervals[i][1] < previous[1]:
                    previous = intervals[i]
            else:
                previous = intervals[i]
        return remove

# Time Complexity: nlogn + n -> O(nlogn)
# Space Complexity: O(n) or can be O(1) because we sorted inplace, talk with interviewer