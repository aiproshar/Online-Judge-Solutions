class MedianFinder(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.max_heap == [] or num < self.max_heap[0] * -1:
            heapq.heappush(self.max_heap, num * -1)
        else:
            heapq.heappush(self.min_heap, num)
        # Rebalancing
        if len(self.max_heap) - len(self.min_heap) > 1:
            val = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, val)
        elif len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val * -1)

    def findMedian(self):
        """
        :rtype: float
        """
        # Corner case, this also handles calling find median on single element stream
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        total = ((self.max_heap[0] * -1) + self.min_heap[0]) / 2.00
        return total

# Time Complexity: find -> O(1) addNum -> logn