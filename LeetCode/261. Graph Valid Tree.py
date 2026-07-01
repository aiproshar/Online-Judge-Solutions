class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A graph is a valid tree if and only if:
        #   (1) it has NO cycle, AND
        #   (2) it is fully connected (all n nodes reachable from one start).
        # This code checks both: cycle detection via DFS coloring,
        # and connectivity via the visited-count check at the end.

        # ---- Step 1: Build an undirected adjacency list ----
        # Each edge [x, y] is bidirectional, so we add y to x's list
        # AND x to y's list.
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        # ---- Step 2: Set up bookkeeping ----
        visited = set()                 # tracks every node we finish processing
        WHITE, GREY, BLACK = 0, 1, 2    # node states:
                                        #   WHITE = not yet visited
                                        #   GREY  = currently on the DFS stack (being explored)
                                        #   BLACK = fully explored (done)
        color = [WHITE] * n             # all nodes start WHITE

        # ---- Step 3: DFS that returns True if it finds a back-edge (cycle) ----
        def dfs(node, parent) -> bool:
            # Mark this node GREY: it's now "in progress" on the current path.
            color[node] = GREY
            visited.add(node)           # record that we've reached this node

            for child in adj_list[node]:
                # Skip the edge we just came from. In an undirected graph,
                # the parent will always appear in the child's list, and
                # walking straight back to it is NOT a real cycle.
                if child == parent:
                    continue

                # If a neighbor is GREY, it's an ancestor still on our path.
                # Reaching it again means we found a back-edge => a cycle.
                if color[child] == GREY:
                    return True

                # If a neighbor is WHITE, it's unexplored: recurse into it.
                # If that recursion finds a cycle, propagate True upward.
                if color[child] == WHITE:
                    if dfs(child, node) is True:
                        return True
                # (A BLACK child is already fully done and safe to ignore.)

            # Finished exploring every neighbor: mark this node BLACK (done).
            color[node] = BLACK
            return False                # no cycle found in this subtree

        # ---- Step 4: Run DFS from node 0 ----
        # If DFS reports a cycle, it can't be a tree.
        if dfs(0, None) is True:
            return False

        # ---- Step 5: Connectivity check ----
        # A single DFS from node 0 reaches every node ONLY if the graph is
        # connected. If some node was never visited, the graph is split into
        # pieces (a forest, not a tree), so it's invalid.
        if len(visited) != n:
            return False

        # Passed both checks: no cycle AND fully connected => valid tree.
        return True

# Time Complexity: O(V+E)
# Space: O(V+E)