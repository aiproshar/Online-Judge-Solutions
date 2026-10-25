'''
This is an example how far i have improved in coding within 6 months, from cpp to python 3 transition
learning to think and code pythonic way and all sort of things. Some time we all should take a pause , look back how far we have
come and maybe a bit of appreciation. My old c++ code was complete BS and dogfood

Solved under 15 minutes, simpler version of task scheduler
Heap + list combined
'''
class Solution:
    def reorganizeString(self, s: str) -> str:

        temp = Counter(s)

        heap = []
        for char, freq in temp.items():
            heap.append([-freq, char])
        # O(k)
        heapq.heapify(heap)

        # CC, not possible
        total = sum(temp.values())
        max_freq = -heap[0][0]
        if total - max_freq < (total // 2):
            return ""

        stream = []

        while heap:
            block = []
            for i in range(2):
                if heap:
                    block.append(heapq.heappop(heap))
            for i in range(len(block)):
                freq, char = block[i]
                stream.append(char)
                freq += 1
                if freq != 0:
                    heapq.heappush(heap, (freq, char))
        return "".join(stream)

# Time Complexity: nlogk, n = len(s) k= 26 so its O(n)
# Space Complexity: O(26) ~ O(1), output O(n)





'''
Generic K slice Solution
SO we can convert this to any stuffs
'''


class Solution:
    def reorganizeString(self, s: str) -> str:

        cnt = Counter(s)
        heap = [(-freq, char) for char, freq in cnt.items()]
        heapq.heapify(heap)
        # slice size
        k = 2
        res = []  # a b
        temp = deque()  #
        while heap:
            for _ in range(k):
                if heap:
                    freq, char = heapq.heappop(heap)
                    temp.append((freq, char))
                else:
                    break

            if len(temp) < k:
                break

            while temp:
                freq, char = temp.popleft()
                freq += 1
                res.append(char)
                if freq < 0:
                    heapq.heappush(heap, (freq, char))

        # last run, must be solo freq
        while temp:
            freq, char = temp.popleft()
            freq += 1
            res.append(char)
            if freq != 0:
                return ""

        return "".join(res)

# Time Complexity: O(n) for initial heapify + O(nlog26)
# Space: O(n)