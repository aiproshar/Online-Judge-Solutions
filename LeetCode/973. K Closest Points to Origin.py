class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key = lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]

# One-liner solution, just sort the array based on lambda, and return the first k elements
# time complexity: O(nlogn)
# Space Complexity: O(n)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        counter = count()
        distances = []
        for x, y in points:
            # OptimizationL distance = x**2 + y**2, avoid floating point operation, if x > y then sqrt(x) > sqrt(y)
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(distances, (distance * -1, next(counter), [x, y]))
            if len(distances) > k:
                heapq.heappop(distances)
        closest = []
        while distances:
            point = heapq.heappop(distances)[2]
            closest.append(point)
        return closest

# Heap based solution
# This is highly efficient in a stream , where n >> k
# Time complexity: O(nlogk)
# Space Complexity: O(k)