class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:

        for interval in self.intervals:

            if interval[0] < endTime and interval[1] > startTime:
                return False
        self.intervals.append((startTime, endTime))
        return True

# Time Complexity: O(n) per booking call
# Space Complexity: O(n)
