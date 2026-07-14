

'''
Top Down Recursive Approach + Memo
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        @cache
        def dp(x, y) -> int:

            res = [0]
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                    if matrix[nx][ny] > matrix[x][y]:
                        res.append(dp(nx, ny))
            return max(res) + 1

        global_max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                global_max = max(global_max, dp(i, j))
        return global_max

# Time Complexity: O(m*n) state space
# Space Complexity: O(m*n) state, note that recursion depth is also m*n (snake zigzag all elements)

'''
BFS Level order + Khans Algorithm Bases Solution

'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        indegree = defaultdict(lambda: 0)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[(nx, ny)] += 1

        que = deque()
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if indegree[(x, y)] == 0:
                    que.append((x, y))

        depth = 0

        while que:
            depth += 1
            for _ in range(len(que)):
                x, y = que.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[(nx, ny)] -= 1
                            if indegree[(nx, ny)] == 0:
                                que.append((nx, ny))
        return depth

# Time Complexity: O(m*n) bunch of two level loops
# Space Complexity: O(m*n)
# O(1) recursion depth, no risk of stack overflow, thats the advantage over dfs+memo version, rest almost same