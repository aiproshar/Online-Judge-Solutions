"""
Such a beautiful problem, elegant
Intervals + heap at work

Let's sort on start time
Heap represents current concurrent meeting going
heap has all previous meetings, if my new meeting starts after previous meeting, we can poop because it's ended
Heap is sorted based on endtimes, so the meeting ends earliest is compared (and we insert or pop)
If not, just push our new meeting increase concurrent meetings
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        max_rooms = 0
        for start, end in intervals:
            # Remove all meetings that ends before the new one, corner case handle empty heap
           # Due to the nature of heap, the meeting ends earliest is heap root, so its guaranteed that we
            # All the meetings that ends early are kicked out
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            # entering the new meeting
            heapq.heappush(heap, end)
            max_rooms = max(max_rooms, len(heap))
        return max_rooms


# Time Complexity: O(nlogn) -> sort + n heap pus.pop each logn, so again O(nlogn + nlogn) -> O(nlogn)
# Scape Complexity:heap can grow as linear, also sort so O(n)

'''
More elegant solution, event sweep based solution
More on coding templates, Intervals section
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        max_concurrent = 0
        events.sort(key=lambda x: (x[0], x[1]))
        current = 0
        for _, val in events:
            current += val
            max_concurrent = max(max_concurrent, current)
        return max_concurrent
# Time Complexity: O(nlogn)
# Space Complexity: O(n)