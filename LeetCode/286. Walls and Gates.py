# BFS with level order traversal
# We do BFS multiple times, because we have many sources (gates)
# Each time we do BFS, we traverse all nodes and try to reduce distance

class Solution:
    def __bfs(self, i, j, rooms: list[list[int]]) -> None:
        queue = deque()
        queue.append((i, j))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        level = 1
        while queue:
            # Needed to know the queue size for level order traversal
            # So can can keep track of level
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]):
                        if 0 < rooms[nx][ny] <= 2147483647 and rooms[nx][ny] > level:
                            rooms[nx][ny] = level
                            queue.append((nx, ny))
            level += 1
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    # do BFS for each gate and try to reduce the distance
                    self.__bfs(i, j, rooms)
        return None
