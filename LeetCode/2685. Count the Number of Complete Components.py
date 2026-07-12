"""
Extremely Important Problem, DSU + Graph Theory Basics
In complete Graph, every node is directly connected to every node,
So, if we have 5 nodes, first node can connect to 4, then 3, then 2. Its n(n+1) // 2 but n is less by 1
So, No of edges on Complete Graph: n(n-1) // 2
Use DSU to find groups, and make sure each group is a complete graph or not
"""
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(node_1, node_2) -> bool:
            root_1 = find(node_1)
            root_2 = find(node_2)
            if root_1 == root_2:
                # Failed to union
                return False
            if rank[root_1] > rank[root_2]:
                parent[root_2] = root_1
            elif rank[root_1] < rank[root_2]:
                parent[root_1] = root_2
            else:
                parent[root_2] = root_1
                rank[root_1] += 1
            return True

        edge_count = defaultdict(lambda: 0)
        for u, v in edges:
            union(u, v)

        # Forced Path compression, all union operations done
        # This is a corner case, imagine a-b-c and d-e-f and we connect c-d
        # Parent of c changes to d, but parent of a and b still is c, so we need compression
        # From that we can do frequency count on parent array, we can find no of nodes on each graph
        # Also use a dict to
        for node in range(n):
            parent[node] = find(node)

        for u, v in edges:
            # U, V does not matter, the part of dame DSU
            # Both Parent Same
            edge_count[parent[u]] += 1


        connected_components = Counter(parent)
        complete_count = 0

        for leader, size in connected_components.items():
            if ((size - 1) * size) // 2 == edge_count[leader]:
                complete_count += 1
        return complete_count

# Time Complexity: O(V+E)
# Space: O(V)