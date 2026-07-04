# This is pure MST in disguise
# We need to construct the edges, the condition makes this a complete graph

'''
Prims Algorithm MST
Generate Adjacency List
Complete Graph
'''


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 0

        points = [tuple(x) for x in points]
        adj_list = defaultdict(lambda: [])

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[points[i]].append((cost, points[j]))
                adj_list[points[j]].append((cost, points[i]))

        heap = [(0, points[0])]
        total_cost = 0
        visited = set()

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            total_cost += cost
            visited.add(node)
            # Early termination, all nodes connected
            if len(visited) == len(adj_list):
                return total_cost
            for weight, child in adj_list[node]:
                if child not in visited:
                    heapq.heappush(heap, (weight, child))
        return -1


# Time complexity: Heap Ops E times ,O(ElogE) or O(N^2logN) //For complete graph E ~ N^2
# Space complexity: O(N^2) //in adj list it's V+E

