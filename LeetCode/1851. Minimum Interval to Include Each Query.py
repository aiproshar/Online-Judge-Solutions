
'''
Default Brute Force Solution
We pick each query, go through each interval, if query is inside interval, is it smallest ?
TLE
'''
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        min_len = defaultdict(lambda: -1)
        for query in queries:
            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    if min_len[query] == -1:
                        min_len[query] = interval[1] - interval[0] + 1
                    else:
                        min_len[query] = min(min_len[query], interval[1] - interval[0] + 1)
        ans = [min_len[query] for query in queries]
        return ans
# Time Complexity: O(M*N) -> Len of Query * Len of Intervals
# Space Complexity: O(n)



'''
Really a true hard problem, lot of optimization here
Step one: For current query, include all the intervals that started before or in query time on a heap
Step two: Now pop the interval with lowest length, and also for same lowest the earliest
          If interval end <= query, means it both starts and ends before query, remove from heap
          So if heap has any value left by now, they guaranteed to be inside interval (or can be empty heap, no interval covers)
          As we sorted the query, all queries are greated, means the value we already discarded is useless in future
 The heap might have more than one value left, we must not remove them. They are guaranteed to contain query,
 and future values might also contain them.
'''

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        queries_sorted = sorted(queries)
        minimum = defaultdict(lambda: -1)
        intervals.sort()
        i = 0
        for query in queries_sorted:
            # Add all that started before
            while i < len(intervals) and intervals[i][0] <= query:
                len_ = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (len_, intervals[i][1]))
                i += 1
            # Remove all that ended before
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            # If heap is not empty, all intervals here contains q
            # As heap is based on the sorted value, top value is all we need
            # The heap values might be utilized by next query who knows, that's why keep them
            if heap:
                minimum[query] = heap[0][0]
        return [minimum[x] for x in queries]

# time complexity: nlogn + qlogq -> Both sort and again nlogn heap operations
# Time: O(nlogn + qlogq)
# Space Complexity: O(n) for heap and O(q) for result dict so O(n+q)