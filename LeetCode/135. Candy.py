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

'''
Two passed based solution with corner case
If i am larger then left i must be atlreast +1 candies than right 
'''
class Solution:
    def candy(self, ratings: list[int]) -> int:

        # initially everyone has single candy
        # We only add extra as necessary
        candies = [1] * len(ratings)

        for i in range(1, len(candies)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(candies) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # corner case, we must take the larger one
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# Time and Space Complexity: O(n)