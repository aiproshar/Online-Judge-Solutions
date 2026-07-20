'''
Solved this while chilling with EXPERIMENTATION ENG TEAM on resort, during weekend
COnsistency is key
This is DFS based soltuion, but a bit inefficient. More details on optimized solution
'''
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(lambda: [])

        for x, y in edges:
            adj_list[x].append(y)

        WHITE, GREY, BLACK = 0, 1, 2

        def dfs(source) -> bool:
            color[source] = GREY

            for child in adj_list[source]:
                if color[child] == GREY:
                    # backedge
                    return True
                if color[child] == WHITE and dfs(child):
                    return True
            color[source] = BLACK
            return False

        for i in range(n):
            color = defaultdict(lambda: WHITE)
            if dfs(i):
                # not a DAG
                return -1
            else:
                # can be champion, check reachable nodes
                # if all nodes are reachable, we have the champion
                if len(color) == n:
                    return i
        return -1

# Time Complexity:

'''
Much Easier Solution, As the statement said its a DAG, we dont need to look for cycle
All we need is find how many indegree 0 (entry point) we have, if we have exactly one with indegree o, we have chap

'''

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:


        indegree = {} # We can also use a list indegree = [0] * n
        for i in range(n):
            indegree[i] = 0

        for x,y in edges:
            indegree[y] += 1
        strongest = [item for item in indegree if indegree[item] == 0]
        # if we use a list: strongest = [idx for idx in range(n) if indegree[idx] == 0]
        if len(strongest) > 1:
            return -1
        return strongest[0]

# Time Complexity: O(V+E)
# Space: O(V)