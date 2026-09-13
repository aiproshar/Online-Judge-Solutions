"""
Hardest problem i solved till date

MST problem, advanced variant. We must use kruskal (DSU) for simplification
We havve 3 Edges -> critical, psudo_critical and not part of any MST

Critical -> Part of each and every MST, skip this, and you fail to build an MST
Psudo Critical -> Part of some MST, but skip this you still can create MST
Others -> We don't care


The idea: Run generic kruskal to find MST cost
Take an edge, skip it and try to build MST. If we fail it's a critiacal edge
If we don't fail, try to build a MST with it, if we can then its psudo critical
Thsts the whole Idea
"""



class Solution:

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def find(node: int, root: list[int]) -> int:
            if root[node] != node:
                root[node] = find(root[node], root)
            return root[node]

        def union(n1: int, n2: int, root: list[int], rank: list[int]) -> bool:
            r1 = find(n1, root)
            r2 = find(n2, root)
            if r1 == r2:
                return False
            if rank[r1] > rank[r2]:
                root[r2] = r1
            elif rank[r2] > rank[r1]:
                root[r1] = r2
            else:
                root[r2] = r1
                rank[r1] += 1
            return True

        for i in range(len(edges)):
            # push the original index
            edges[i].append(i)

        edges.sort(key=lambda x: x[2])

        minimum_cost = 0
        rank = [1] * n
        root = [x for x in range(n)]
        for n1, n2, cost, _ in edges:
            if union(n1, n2, root, rank):
                minimum_cost += cost
        critical = []
        psudo_critical = []

        for k in range(len(edges)):
            # Test Critical
            # Are we able to build a MST with skipping Kth edge
            rank = [1] * n
            root = [x for x in range(n)]
            current_cost = 0
            edge_count = 0
            for i in range(len(edges)):
                if i == k:
                    continue
                n1, n2, cost, _idx = edges[i]
                if union(n1, n2, root, rank):
                    current_cost += cost
                    edge_count += 1

            if current_cost != minimum_cost:
                # we cannot built an MST without this k, we need this
                # Its critical
                critical.append(edges[k][3])
            else:
                # We were able to build MST without it
                # But is it part of some MST ? Or its not needed for any MST
                # If its part of some MST, we can build a MST by forcefully choosing this first
                # Can we build one with it ? If yes its psudo critical
                rank = [1] * n
                root = [x for x in range(n)]

                # Forcing to pick K first
                n1, n2, cost, _ = edges[k]
                current_cost = cost
                union(n1, n2, root, rank)
                for i in range(len(edges)):
                    n1, n2, cost, _ = edges[i]
                    if union(n1, n2, root, rank):
                        current_cost += cost
                if current_cost == minimum_cost:
                    psudo_critical.append(edges[k][3])
        return [critical, psudo_critical]

# Time Complexity: ElogE for sorting, E^2 for MST build by enforce/skip E
# Space Complexity: O(E)