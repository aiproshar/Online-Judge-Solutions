
'''
Bellman Ford based solution
Variation: Stop bleeding. Each iteration, we only want to forward one level, that's why we update on future array
This has no effect on ordering of edges
One corner case, temp[v] might be updated several time, for example,
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        distance = defaultdict(lambda: math.inf)
        distance[src] = 0

        for _ in range(k+1):
            temp = distance.copy()
            for u, v, cost in flights:
                # Corner Case, we might update same temp v multiple times,
                # With one extra path relaxation we able to reach some destination many ways
                # We must pick the shortest
                if temp[v] > distance[u] + cost:
                    temp[v] = distance[u] + cost
            distance = temp
        if distance[dst] == math.inf:
            return -1
        return distance[dst]
# Time Complexity: O(k * E) where E can be from N -> N^2
# Space Complexity: O(N)


'''
BFS inspired approach, but the first one is better
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = defaultdict(lambda: [])
        for u, v, cost in flights:
            adj_list[u].append((cost, v))
        que = deque()
        que.append((0, src))
        distance = defaultdict(lambda: math.inf)
        distance[src] = 0
        while k+1 > 0 and que:
            lvl_depth = len(que)
            k -= 1
            temp = distance.copy()
            for _ in range(lvl_depth):
                cost, current = que.popleft()
                for child_cost, child in adj_list[current]:
                    if cost + child_cost < temp[child]:
                        temp[child] = cost + child_cost
                        que.append((temp[child], child))
            distance = temp
        return distance[dst] if dst in distance else -1

# Time 