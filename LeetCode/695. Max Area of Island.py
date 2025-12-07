# 99% same as leetcode 200
# Instead of calculating the number of islands, we are saving the largest island
# Basic BFS 
# More on leetcode 200


class Solution:
    def __bfs(self, i, j, grid: list[list[str]]) -> None:
        queue = deque()
        queue.append((i, j))
        # We start from one, because the source node is also part of the island, at least 1 size
        area = 1
        grid[i][j] = 0
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
                    area += 1
        return area


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    mx = self.__bfs(i, j, grid)
                    max_area = max(max_area, mx)
        return max_area
