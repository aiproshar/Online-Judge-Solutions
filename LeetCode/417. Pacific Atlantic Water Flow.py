# Multi Source BFS
# We keep track of visited/reachable from pacific and atlantic end
# We do set intersection to find cells from which water flows to both ocean
# The idea is reverse the question, instead of going to every cell and find which ocen it can reach, we
# calculate from this ocean where we can reach. We add all the shoreline cells as bfs sources


class Solution:
    def _bfs(self, sources: list[tuple[int, int]], heights: list[list[int]]) -> set[tuple[int, int]]:

        que = deque()
        visited = set()
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for source in sources:
            que.append(source)
            visited.add(source)

        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]):
                    if heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        que.append((nx, ny))
                        visited.add((nx, ny))
        return visited

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_sources = []
        atlantic_sources = []

        # pacific Sources
        i = 0
        for j in range(len(heights[0])):
            pacific_sources.append((i, j))
        j = 0
        for i in range(len(heights)):
            pacific_sources.append((i, j))

        # Atlantic Sources
        i = len(heights) - 1
        for j in range(len(heights[0])):
            atlantic_sources.append((i, j))
        j = len(heights[0]) - 1
        for i in range(len(heights)):
            atlantic_sources.append((i, j))

        both = self._bfs(pacific_sources, heights) & self._bfs(atlantic_sources, heights)
        return [list(x) for x in both]



# Time Complexity: BFS, O(MN)
# Space Complexity: O(MN)