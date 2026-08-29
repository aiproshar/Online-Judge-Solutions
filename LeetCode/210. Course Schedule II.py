
# Topological Sort implementation using DFS
# Also checks for cycle, thats the important part
# If we dont check cycle, we still retuan a sorted list of vertexes, but thats invalid


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        adj_list = defaultdict(list)

        for y, x in prerequisites:
            adj_list[x].append(y)
        color = [WHITE] * numCourses
        finish_time = []
        # True means cycle present
        def dfs(source: int) -> bool:
            color[source] = GREY
            for child in adj_list[source]:
                if color[child] == GREY:
                    return True
                if color[child] == WHITE and dfs(child):
                    return True
            color[source] = BLACK
            finish_time.append(source)
            return False

        for i in range(numCourses):
            # We are trying to detect a cycle
            # We must go through all the nodes because of possibility of disconnected graph
            # invoke dfs on all disconnected graph
            if color[i] == WHITE:
                if dfs(i):
                    # cycle detected, as per Problem Statement return []
                    return []
        return finish_time[::-1]
# Time: O(V+E)
# Space: O(V+E)
# Stack overflow risk in linked list like graph



'''
Khans algorithm using BFS
More easier, this dont have recursion depth problem
We need to make sure all nodes are visited, even they dont appear in edge relation, for example courses who dont have any dependency
Because they must be present at the order
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        for y, x in prerequisites:
            adj_list[x].append(y)
            indegree[y] += 1
        order = []
        que = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        while que:
            node = que.popleft()
            order.append(node)
            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)

        if len(order) == numCourses:
            return order
        return []

# Time Complexity: O(V+E)
# Space: O(V+E) -> adj list,  O(V) -> indegree array,  O(V) -> que, order -> O(v)