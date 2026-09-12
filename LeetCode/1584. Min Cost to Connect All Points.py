# This is pure MST in disguise
# We need to construct the edges, the condition makes this a complete graph

'''
Prims Algorithm MST
Dense Graph, Generate childs on the FLY
Also early termination

This is updated solution, which does not create adj list and faster with early termination
'''

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()
        heap = [(0, points[0][0], points[0][1])]
        total_cost = 0
        while heap:
            cost, x, y = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            total_cost += cost
            # only mark as visited during deque time
            visited.add((x, y))
            if len(visited) == len(points):
                break
            for i, j in points:
                if (i, j) not in visited:
                    dist = abs(x - i) + abs(y - j)
                    # We might enque later with lower cost, so dont mark it
                    heapq.heappush(heap, (dist, i, j))
        return total_cost
# E = V^2 as complete graph
# Time Complexity: O(ElogE), O(ElogV^2) -> O(ElogV)




# Kruskal's Algorithm
# Faster on sparse graphs
# 95% code is DSU + for loop
# We don't need adj list here, we need all edges in a single list (cost, u, v)
# Only undirected only

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        rank = [1] * n
        parent = [x for x in range(n)]
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(n1, n2) -> bool:
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return False
            if rank[r1] > rank[r2]:
                parent[r2] = r1
            elif rank[r2] > rank[r1]:
                parent[r1] = r2
            else:
                parent[r2] = r1
                rank[r1] += 1
            return True
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([cost, i, j])
        edges.sort()
        total_cost = 0
        edges_count = 0
        for cost, x, y in edges:
            if union(x, y):
                total_cost += cost
                edges_count += 1
                # Early termination
                if edges_count == n - 1:
                    break
        return total_cost

# Time Complexity: O(E) to create all the edges, O(ElogE) for sort
# Space: O(E)