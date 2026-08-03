"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

'''
Standard Line Sweep Algorithm
We just need to find the gaps where there is no interval, you know what i mean
There is another way to solve this, using heaps and bla bla, but that assumes
- No overlap on each employees intervals
- Already sorted

Our solution is general purpose, dont care if there is overlaps on each employees interval or no order
'''
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        merged = []
        for x in schedule:
            for interval in x:
                merged.append([interval.start, interval.end])
        # Sorting based on start time for line sweep algorithm
        merged.sort(key=lambda item: item[0])

        last_end = merged[0][1]
        freetime = []
        for start, end in merged[1:]:
            if start <= last_end:
                # time to extend
                last_end = max(last_end, end)
            else:
                # We find a free window, cause next interval starts after current one ends
                freetime.append(Interval(last_end, start))
                last_end = end
        return freetime
# N -> total intervals sum
# Time Complexity: O(NlogN) -> sort
# Space: O(N)


