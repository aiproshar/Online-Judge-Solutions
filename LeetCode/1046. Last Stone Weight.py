class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if x == y:
                continue
            else:
                heapq.heappush(stones, -1 * (x - y))

        if stones:
            return stones[0] * -1
        else:
            return 0
# Time Complexity: O(n) + O(nlogn)
# Space Complexity: O(n)