# Multi Source BFS
# We keep track of visited/reachable from pacific and atlantic end
# We do set intersection to find cells from which water flows to both ocean
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(heights, sources: list[tuple[int, int]]) -> set:
            que = deque()
            visited = set()
            for source in sources:
                que.append(source)
                visited.add(source)
            direction = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]
            while que:
                x, y = que.popleft()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]):
                        if heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            que.append((nx, ny))
            return visited

        # Pacific
        pacific = set()
        edges = []
        for j in range(len(heights[0])):
            edges.append((0, j))
        for i in range(len(heights)):
            edges.append((i, 0))
        pacific = bfs(heights, edges)

        # Atlantic
        atlantic = set()
        edges = []
        for j in range(len(heights[0])):
            edges.append((len(heights) - 1, j))
        for i in range(len(heights)):
            edges.append((i, len(heights[0]) - 1))
        atlantic = bfs(heights, edges)
        res = list(pacific & atlantic)
        return res

# Time Complexity: O(m*n) -> each cell is visited once
# Space Complexity: O(m*n) -> maximum no we can have in visited set/queue