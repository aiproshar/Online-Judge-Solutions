
'''
There are many different ways to sort an array, manually or using built in sort/heap libraries
Please go here for full describption/breakdown and other methods, this is just a reference
Link: https://github.com/aiproshar/coding-templates/blob/main/sort_heap.md
'''

class Heap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1
        # bubble up
        while i > 0:
            parent = (i - 1) // 2
            if parent >= 0 and self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break
        return

    def __bool__(self):
        return bool(self.heap)

    def pop(self) -> int:
        if not self.heap:
            return None
        ans = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        # bubble down
        while i < len(self.heap):
            idx = i
            left = (i * 2) + 1
            right = (i * 2) + 2
            if left < len(self.heap) and self.heap[left] < self.heap[idx]:
                idx = left
            if right < len(self.heap) and self.heap[right] < self.heap[idx]:
                idx = right
            if idx != i:
                self.heap[i], self.heap[idx] = self.heap[idx], self.heap[i]
                i = idx
            else:
                break
        return ans


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        heap = Heap()
        for num in nums:
            heap.push(num)
        ans = []
        while heap:
            ans.append(heap.pop())
        return ans

# Time and Space: Refer to linked doc