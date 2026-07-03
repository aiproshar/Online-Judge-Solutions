'''
Simple Cycle detection on an undirected graph, BFS/DFS will work but bad complexity

Ideal problem for DSU
Just union them, if we fail to union them, means they already connected otherwise, a cycle
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [item for item in range(len(edges))]
        rank = [0 for _ in range(len(edges))]
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(node_1, node_2)-> bool:
            root_1 = find(node_1)
            root_2 = find(node_2)

            if root_1 == root_2:
                return False
            if rank[root_1] > rank[root_2]:
                parent[root_2] = root_1
            elif rank[root_1] < rank[root_2]:
                parent[root_1] = root_2
            else:
                parent[root_2] = root_1
                rank[root_1] += 1
            return True

        res = []
        for x,y in edges:
            if union(x-1, y-1) is False:
                # A bit redundant, we can do termination because there is only one redundant edge
                # But if there were more than one this would have returned the last one
                res =  [x, y]
        return res

# Time: O(N), as union operations are constant, and we do N of these
# Space: O(N) -> some extra for leader and rank