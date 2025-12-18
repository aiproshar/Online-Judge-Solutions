# DFS recusrise exploration edge detection
# Grey Nodes -> Current Stack, Black Nodes -> Fully explored all childs
# White nodes -> Untouched
# We can get way by just exploring from single node, but if its not a Strongly Connected
# To solve the sparse problem we check all the nodes and explore 
class Solution:

    def __dfs(self, source, adj_list: defaultdict(list), color: list) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2
        # This is important, dont forget to put the current node into the stack
        # AKA marking as GREY
        color[source] = GREY
        for child in adj_list[source]:
            if color[child] == GREY:
                return True
            if color[child] == WHITE and self.__dfs(child, adj_list, color):
                return True
        color[source] = BLACK
        return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        WHITE, GREY, BLACK = 0, 1, 2
        for rel in prerequisites:
            adj_list[rel[1]].append(rel[0])
        color = [WHITE] * numCourses

        for course in range(numCourses):
            if color[course] == WHITE:
                # We are trying to detect a cycle
                # We must go through all the nodes because of possibility of sparse graph
                if self.__dfs(course, adj_list, color) is True:
                    return False
        return True
