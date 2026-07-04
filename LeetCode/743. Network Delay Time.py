# Basic Dijkstra, Single source all pair shortest path
# Min Heap, greedy implementation

class Solution:
    def dijkstra(self, adj_list: list[tuple], source, n) -> defaultdict:
        # math.inf is the pythonic way to declare INF, no C++ BS here.
        # Initially, distance to all node is infinite, also means unreachable
        distance = [math.inf for _ in range(n + 1)]
        # Start point, self distance is zero
        distance[source] = 0

        # Our heap, which stores all nodes to explore, also with their distance
        # We sort based on distance, nodes with lowest distance pooped first
        # Then we try to do path relaxation from there
        # Each node is only poped once, so we keep track of that in a visited array
        # But there can be multiple ways means distance value and destination to same node
        # Example -> (2,6), (4,6), (7,6) -> All path goes to 6th node, but different distance value
        # sortes one gets pooped
        heap = []
        heap.append((0, source))
        visited = set()
        while heap:
            dist, u = heapq.heappop(heap)
            if u in visited: # We can also replace this two lines with: if dist > distance[u] continue
                continue
            visited.add(u)
            for cost, v in adj_list[u]:
                if distance[u] + cost < distance[v]:
                    distance[v] = distance[u] + cost
                    heapq.heappush(heap, (distance[v], v))
        return distance
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, cost in times:
            adj_list[u].append((cost, v))
        distance = self.dijkstra(adj_list, k, n)
        max_dist = max(distance[1::])
        return max_dist if max_dist < math.inf else -1



'''
Cleaner Solution
'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(lambda: [])
        for u, v, w in times:
            adj_list[u - 1].append((w, v - 1))
        distance = [math.inf] * n
        heap = []
        distance[k - 1] = 0
        heapq.heappush(heap, (0, k - 1))
        while heap:
            dist, u = heapq.heappop(heap)
            if dist > distance[u]:
                continue
            for cost, v in adj_list[u]:
                if distance[u] + cost < distance[v]:
                    # path relaxation
                    distance[v] = distance[u] + cost
                    heapq.heappush(heap, (distance[v], v))

        return max(distance) if max(distance) != math.inf else -1
# Time Complexity: O(ElogV)
# Space Complexity: O(V+E)

