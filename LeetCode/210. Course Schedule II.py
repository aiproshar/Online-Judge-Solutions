
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
