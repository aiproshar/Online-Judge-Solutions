# DFS recursive exploration edge detection
# Grey Nodes -> Current Stack, Black Nodes -> Fully explored all children
# White nodes -> Untouched
# We can get way by just exploring from single node, but if it's a disconnected graph
# To solve the sparse problem we check all the nodes and explore

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        WHITE, GREY, BLACK = 0, 1, 2
        adj_list = defaultdict(list)

        for y, x in prerequisites:
            adj_list[x].append(y)
        color = [WHITE] * numCourses

        # True means cycle present
        def dfs(source: int) -> bool:
            color[source] = GREY
            for child in adj_list[source]:
                if color[child] == GREY:
                    return True
                if color[child] == WHITE and dfs(child):
                    return True
            color[source] = BLACK
            return False

        for i in range(numCourses):
            # We are trying to detect a cycle
            # We must go through all the nodes because of possibility of disconnected graph
            if color[i] == WHITE:
                if dfs(i):
                    return False
        return True

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)
# Real risk: Recursion depth, stack overflow for skewed trees which are closed to a linkedlist

'''
Kahn's algorith based solution
Indegree based, this is a variation of BFS
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for y, x in prerequisites:  # edge from x -> y
            adj_list[x].append(y)
            indegree[y] += 1

        que = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        while que:
            node = que.popleft()
            # We finish the node task
            completed += 1
            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)
        return completed == numCourses

# Time Complexity: O(V+E)
# Space Complexity: O(V+E)