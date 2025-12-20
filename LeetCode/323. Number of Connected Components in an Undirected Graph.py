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
    
    # made a big mistake, all unioun operation must be done on the root
    def union(self, node1: int, node2: int, parent: list[int], rank: list[int]) -> bool:

        # Calculate the root, dont use the node in any operations after
        # The nodes only purpose is to calculate its root thats it
        root1 = self.find(node1, parent)
        root2 = self.find(node2, parent)
        if root1 == root2:
            return False
        if rank[root1] >= rank[root1]:
            parent[root2] = root1
            rank[root1] += 1
        else:
            parent[root1] = root2
            rank[root2] += 1
        return True
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1 for x in range(n)]

        no_dsu = n
        for x, y in edges:
            if self.union(x, y, parent, rank):
                no_dsu -= 1
        return no_dsu
