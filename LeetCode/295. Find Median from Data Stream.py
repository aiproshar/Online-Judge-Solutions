class MedianFinder(object):

    def __init__(self):
        self.max_heap = [] #first half
        self.min_heap = [] #second half

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, num * -1)
            return
        
        #handles corner case
        #some may suggest lest just insert into maxheap or minheap and rebalance
        #This creates aproblem, 1,2,3,4 ->MaxHeap and 9,10,11,12 ->minHeap, we enter 100 here to maxheap, now hax_heap.top == 100, and rebalance
        #also not triggered, as differenc of 1 is allowed, now median is  100 + 9 / 2.00, we cooked
        #Always we make sure current value falls into the heap range , or we cooked
        if num > self.max_heap[0] * -1:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num * -1)
        
        #balancing
        if len(self.max_heap) - len(self.min_heap) > 1:
            top = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, top)
        if len(self.min_heap) > len(self.max_heap):
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, top * -1)

    def findMedian(self):
        """
        :rtype: float
        """
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return self.max_heap[0] * -1
        else:
            return (self.max_heap[0] * -1 + self.min_heap[0])/2.00
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()