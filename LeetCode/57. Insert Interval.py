"""
Insert Interval (LeetCode 57)

Think of intervals on a number line. There are only 3 relationships
between an existing interval and the new one:

  1. Completely before  →  it ends before new starts
  2. Overlapping        →  everything in between
  3. Completely after   →  it starts after new ends

The trick: we don't need to check for overlap directly.
We just check for "before" and "after" — everything else MUST overlap.
"""
class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:

        res = []
        i = 0

        # PHASE 1: Intervals that come entirely BEFORE new
        #
        # If an interval ENDS before new even STARTS, there's no overlap.
        #   e.g. interval = [1,3], new = [5,8]
        #        interval ends at 3, new starts at 5 → no touching
        #
        # So: interval[end] < new[start] means "completely before"
        while i < len(intervals) and intervals[i][1] < new[0]:
            res.append(intervals[i])
            i += 1

        # PHASE 2: Intervals that OVERLAP with new
        #
        # Now think about it from the other side:
        # An interval that comes entirely AFTER new would START after new ENDS.
        #   i.e. interval[start] > new[end] means "completely after"
        #
        # So the opposite — interval[start] <= new[end] — means
        # "NOT completely after", which means it MUST overlap,
        # because we already handled "completely before" in phase 1.
        #
        # For each overlapping interval, we grow 'new' to swallow it:
        #   - take the smaller start (stretch left)
        #   - take the larger end (stretch right)
        while i < len(intervals) and intervals[i][0] <= new[1]:
            new[0] = min(new[0], intervals[i][0])
            new[1] = max(new[1], intervals[i][1])
            i += 1

        # Done merging — add the (possibly grown) new interval
        res.append(new)

        # PHASE 3: Everything left starts AFTER new ends — just add them
        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
# Time Complexity: O(n)
# Space: O(1) , can also be O(n) because we create a new return array
