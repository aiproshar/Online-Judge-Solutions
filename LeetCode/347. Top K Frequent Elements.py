
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums) # O(n)
        sorted_freq = sorted(nums_freq.items(), key=lambda x: x[1], reverse=True) # O(nlogn)
        top_k = []
        for num in sorted_freq:
            top_k.append(num[0])
            if len(top_k) == k:
                break
        return top_k

# Time Complexity: O(nlogn)
# space complexity: O(n)
'''
The problem with sorting approach is if k = 5 and n=10000000, we are inefficient
Unnecessary sort for rest 9999995 items, we dont care about their order, we care top 5

If we want top 5, we can use minheap, which will kick out the lowest values via pop
When heap size exceeds k, we kick one item

For Top K minimum item, we use MaxHeap, and pop Max items
Simple yet beautiful
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        heap = []
        for item, freq in freq_dict.items():
            heapq.heappush(heap, (freq, item))
            if len(heap) > k:
                heapq.heappop(heap)
        top_k_elem = [x[1] for x in heap]
        return top_k_elem
# Time Complexity: O(n * logk) -> n pushes, heap size constant so log K each push
# Space complexity: O(n)