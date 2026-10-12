'''
Heap Based solution, came up on my own
Simulation Based Solution
'''
class Solution:
    def candy(self, ratings: list[int]) -> int:

        # add sentinels
        ratings = [math.inf] + ratings + [math.inf]
        candies = [0] * len(ratings)

        heap = []

        for i in range(1, len(ratings) - 1):
            heapq.heappush(heap, (ratings[i], i))

        while heap:
            _, idx = heapq.heappop(heap)

            if ratings[idx - 1] >= ratings[idx] and ratings[idx + 1] >= ratings[idx]:
                candies[idx] = 1
            elif ratings[idx - 1] < ratings[idx] and ratings[idx + 1] >= ratings[idx]:
                candies[idx] = candies[idx - 1] + 1
            elif ratings[idx - 1] >= ratings[idx] and ratings[idx + 1] < ratings[idx]:
                candies[idx] = candies[idx + 1] + 1
            else:
                candies[idx] = max(candies[idx + 1], candies[idx - 1]) + 1
        return sum(candies)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)