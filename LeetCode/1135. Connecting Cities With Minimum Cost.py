# Prims algorithm - > Basic Implementation
# Calculating the cost of minimum spanning tree

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for x, y, cost in connections:
            adj_list[x].append((cost, y))
            adj_list[y].append((cost, x))
        source = 1
        visited = {source}
        heap = []
        total_cost = 0
        for cost, dest in adj_list[source]:
            heapq.heappush(heap, (cost, dest))
        while heap:
            cost, vertex = heapq.heappop(heap)
            if vertex not in visited:
                total_cost += cost
                visited.add(vertex)
                for cost, child in adj_list[vertex]:
                    if child not in visited:
                        heapq.heappush(heap, (cost, child))
        if len(visited) != n:
            return -1
        return total_cost

# Time Complexity: We run the loop E times, and a heap push and pop operation there (logE). So O(ElogE)
# Space Complexity: Adj List: O(V+E)