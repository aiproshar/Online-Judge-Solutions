class Solution:
    # Basic DFS, with cycle detection
    # Returns True upon cycle detection
    # Corner Case -> As this is undirected graph, one of our child will be parent
    # We pass the parent node id, so during traversal we dont detect a false cycle
    def __dfs(self, source, previous) -> bool:
        for child in self.adj_list[source]:
            if child == previous:
                continue
            if child in self.visited:
                return True
            self.visited.add(child)
            if self.__dfs(child, source) is True:
                return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adj_list = defaultdict(list)
        for x, y in edges:
            self.adj_list[x].append(y)
            self.adj_list[y].append(x)
        self.visited = {0}
        has_cycle = self.__dfs(0, None)

        if has_cycle is True:
            return False
        # Edge Case: Forest. Multiple Tree or other disconnected graphs can be present
        # For a undirected tree all nodes will be explored during dfs/bfs
        if len(self.visited) != n:
            return False
        return True

        # Time Complexity: All Vertex And Their Edges, once. So O(V+E)
        # Space Complexity: O(V) -> Tree is a linked list, so max depth is all nodes, but also O(V+E) for adj list
