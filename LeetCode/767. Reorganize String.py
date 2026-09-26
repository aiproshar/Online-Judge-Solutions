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

        heap = [(-freq, char) for char, freq in Counter(s).items()]
        heapq.heapify(heap)
        # slice length
        k = 2
        current = []
        # EOL marker, we considering the last run, where we can have any items
        EOL = False
        while heap:
            temp = []
            for _ in range(k):
                if not heap:
                    if EOL:
                        return ""
                    else:
                        EOL = True
                        break
                count, char = heapq.heappop(heap)
                current.append(char)
                temp.append([count, char])

            while temp:
                count, char = temp.pop()
                count += 1
                if count < 0:
                    heapq.heappush(heap, (count, char))

        return "".join(current)

# Time Complexity: O(n) for initial heapify + O(nlog26)
# Space: O(n)