class Solution:
    # multi source BFS, pass all the sources together
    def _bfs(self, sources: list[tuple[int, int]], rooms) -> None:
        INF = 2147483647
        que = deque(sources)
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
                if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]):
                    '''
                    The below code is overkill, as this becomes close to dijkstra
                    By the nature of BFS, we always visit closest nodes first
                    So our update will be optimal the very first try, no subsequent update is required

                    if rooms[nx][ny] > 0 and rooms[x][y] + 1 < rooms[nx][ny]:
                        rooms[nx][ny] = rooms[x][y] + 1
                        que.append((nx, ny))
                    '''
                    if rooms[nx][ny] == INF:
                        rooms[nx][ny] = rooms[x][y] + 1
                        que.append((nx, ny))

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        sources = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    sources.append((i, j))
        self._bfs(sources, rooms)

# Time Complexity: O(M*N)
# Space Complexity: O(M*N)