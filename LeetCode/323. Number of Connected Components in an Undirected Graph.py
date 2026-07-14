# BFS exploration
# If we dont visit all the nodes, that means there are more than one component
# We take the first unvisited node, run BFS and explore
# If we find another unvisited not, that was not visited previous exploration, that means its a disconnected graph
# Each time we encounter means its a component, increment variable
class Solution:
    def __bfs(self, adj_list: defaultdict[int, list], visited: set[int], source) -> None:
        que = deque()
        visited.add(source)
        que.append(source)
        while que:
            parent = que.popleft()
            for child in adj_list[parent]:
                if child not in visited:
                    visited.add(child)
                    que.append(child)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        visited = set()
        graph_count = 0
        for vertex in range(n):
            if vertex not in visited:
                self.__bfs(adj_list, visited, vertex)
                graph_count += 1
        return graph_count

# Time complexity: O(V+E)
# Space Complexity: O(V+E) for adjacency list, O(V) for que and visited set


#
#
# ------------------------------------------ DSU IMPLEMENTATION------------------------
#
#


# Basic DSU, we define union and find method

class Solution:
    def find(self, node: int, parent: list[int]) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    
    # made a big mistake, all union operation must be done on the root
    class Solution:
        def countComponents(self, n: int, edges: List[List[int]]) -> int:
            parent = [i for i in range(n)]
            rank = [0 for i in range(n)]

            def find(node: int, parent: list):
                if parent[node] != node:
                    parent[node] = find(parent[node], parent)
                return parent[node]

            def union(x, y, parent, rank) -> bool:
                rx = find(x, parent)
                ry = find(y, parent)

                if rx == ry:
                    return False
                if rank[rx] > rank[ry]:
                    parent[ry] = rx
                elif rank[ry] > rank[rx]:
                    parent[rx] = ry
                else:
                    rank[rx] += 1
                    parent[ry] = rx
                return True

            distinct = n
            for vx, vy in edges:
                if union(vx, vy, parent, rank):
                    distinct -= 1
            return distinct