
# Topological Sort implementation using DFS
# Also checks for cycle, thats the important part
# If we dont check cycle, we still retuan a sorted list of vertexes, but thats invalid


class Solution:
    def __dfs(self, source) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2
        self.color[source] = GREY
        for child in self.adj_list[source]:
            if self.color[child] == GREY:
                return True
            if self.color[child] == WHITE and self.__dfs(child):
                return True
        self.color[source] = BLACK
        self.order.append(source)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        WHITE, GREY, BLACK = 0, 1, 2
        self.adj_list = defaultdict(list)

        for dest, source in prerequisites:
            self.adj_list[source].append(dest)
        self.order = []
        self.color = [WHITE] * numCourses

        for source in range(numCourses):
            if self.color[source] == WHITE:
                cycle = self.__dfs(source)
                if cycle is True:
                    return []
        # We need to reverse
        return self.order[::-1]

# Time: O(V+E)
# Space: O(V+E)



'''
Khans algorithm using BFS
More easier, this dont have recursion depth problem
We need to make sure all nodes are visited, even they dont appear in edge relation, for example courses who dont have any dependency
Because they must be present at the order
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(lambda: [])
        indegree = [0] * numCourses

        for x, y in prerequisites:
            adj_list[y].append(x)
            indegree[x] += 1
        order = []
        que = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        while que:
            node = que.popleft()
            order.append(node)
            for child in adj_list[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)

        if len(order) == len(indegree):
            return order
        return []

# Time Complexity: O(V+E)
# Space: O(V+E) -> adj list,  O(V) -> indegree array,  O(V) -> que, order -> O(v)