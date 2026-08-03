'''
SWEEP LINE variation, instead of extending(union) we de intersect
Only keep the intersect, makes it smaller over and over until next ballon cannot be put on to intersect
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        # Initially first baloon is the whole intersect
        overlap = points[0]
        arrows = 1

        for start, end in points[1:]:
            # We have overlap, we must shoot arrow in the intersect range
            if overlap[0] <= end and overlap[1] >= start:
                overlap[0] = max(overlap[0], start)
                overlap[1] = min(overlap[1], end)
            else:
                # nah, not possible to pop both baloon with single arrow, refresh
                overlap = [start, end]
                # New arrow for the ballon
                arrows += 1
        return arrows
# Time Complexity: O(nlogn)
# Space: O(1) , if we count built in sort its o(logn) -> O(n)


'''
End time based solution, sort by end time
If next one starts before current one ends, means its a overlap, we imagine shooting at the end
Lot of edge cases gets filtered out due to end time based sorting
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        last = points[0][1]
        arrows = 1
        for start, end in points[1:]:
            if start > last:
                arrows += 1
                last = end
        return arrows