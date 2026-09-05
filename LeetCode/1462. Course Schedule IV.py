'''
Initial Solution, came up pretty fast. DFS + DP YaY
We create a dfs(source) which returns a set of nodes who are reachable from source, transitive nodes
We use memoization to avoud repetative transitive exploration
'''


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        adj_list = defaultdict(list)

        for x, y in prerequisites:
            adj_list[x].append(y)


        # returns all reachable nodes from parent
        # If there is a cycle this will trigger infinite recursion, problem statement guarantees no cycle
        # @cache for memoization, so we calculate same transitive again and again
        @cache
        def dfs(parent) -> set[int]:
            res = set()
            for child in adj_list[parent]:
                '''
                Alternative inplace set operations and slightly faster
                res.add(child) #inplace add single element
                res.update(dfs(child)) #inplace add iterable
                '''
                res = res | dfs(child) | {child}
            return res

        res = []
        for x, y in queries:
            if y in dfs(x):
                res.append(True)
            else:
                res.append(False)
        return res

# Time Complexity: O(V+E) for adj list creation, dfs calculates V times exactly due to cache, and each call its O(VE)
# each query is constant per lookup, so its O(q). in total its O(VE+q)

#Space Complexity: O(V^2 + Q)


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        matrix = [[False] * numCourses for _ in range(numCourses)]

        for x, y in prerequisites:
            matrix[x][y] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        res = []
        for x, y in queries:
            res.append(matrix[x][y])

        return res

# Time Complexity: O(n^3 + q), where q is no of queries, each one constant time
# Space Complexity: O(n^2 + q)