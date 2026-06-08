

"""
Sort and return the kth largest, as default sort is ascending, use negative index, it also solves 0 index problem
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
# Time Complexity: O(nlogn)
# Space: O(n)



'''
Heap based solution, its quite fast when n >> k

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num )
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# Time Complexity: O(nlogk)
# Space Complexity: O(k)