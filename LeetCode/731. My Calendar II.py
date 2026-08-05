'''
Event Sweep Algorithm
'''

class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:

        temp = self.events[:]
        temp.append((start, 1))
        temp.append((end, -1))
        temp.sort()
        mx = 0
        for event in temp:
            mx = mx + event[1]
            if mx > 2:
                return False
        self.events.append((start, 1))
        self.events.append((end, -1))
        self.events.sort()
        return True

# Time Complexity: O(nlogn) on each add
# Space: O(n)

'''
Just an alternative, but does nothing useful here
There is an alternative greedy way on linear , which only works for 3 or more detection
Our works on any no of overlaps

'''
class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:

        temp = self.events[:]
        heapq.heappush(temp, (start, 1))
        heapq.heappush(temp, (end, -1))

        mx = 0
        while temp:
            mx += temp[0][1]
            heapq.heappop(temp)
            if mx > 2:
                return False
        heapq.heappush(self.events, (start, 1))
        heapq.heappush(self.events, (end, -1))
        return True

# Time Complexity: O(nlogn)