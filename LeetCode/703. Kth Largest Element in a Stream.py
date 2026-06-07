"""
Basic Heapq, default heap Min Heap in python
For M max elements, we use min heap, because if pops out the minimum numbers, maximums stays
For Minimum elements, use max heap, if poops the max elements so the minimums stays in the stream


Think of a heap as some kind of buffer stream, no FIFO or LIFO, it captures top Most or bottom Most in the buffer, also pops out streams
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Time Complexity: O(n)  for init, then (n-k)logn for removing elements
# Time Complexity: O(logn) for each push operation


# Space Complexity: O(k) during init (trim off), constant during push