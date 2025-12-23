# This is pure MST in disguise
# We need to construct the edges, the condition makes this a complete graph
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        points = [tuple(x) for x in points]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[points[i]].append((cost, points[j]))
                adj_list[points[j]].append((cost, points[i]))
        # picking first node as starting point
        visited = {points[0]}
        heap = []
        counter = count()
        for cost, dest in adj_list[points[0]]:
            heapq.heappush(heap, (cost, next(counter), dest))
        total_cost = 0
        while heap:
            # This is an important optimization for dense graph
            # I learned this from neetcode explain video
            # As our graph is fully connected, time complexity will be O(ElogE) oe (n^2logn)
            # For fully connected graph, E ~ V^2
            # The time complexity remains same, but average complexity improves
            # The runtime halved in leetcode (1431ms vs 3511ms)
            if len(visited) == len(points):
                break
            cost, _, point = heapq.heappop(heap)
            if point not in visited:
                visited.add(point)
                total_cost += cost
                for dest_cost, dest_point in adj_list[point]:
                    if dest_point not in visited:
                        heapq.heappush(heap, (dest_cost, next(counter), dest_point))
        return total_cost
# Time complexity: Heap Ops E timnes ,O(ElogE) or O(N^2logN) //For complete graph E ~ N^2
# Space complexity: O(N)