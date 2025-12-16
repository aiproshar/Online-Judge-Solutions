# Corner case: There can be more then one rotten orange
# There can be isolated groups, like islands, making this a multi-graph
# in multi-graph each good orange is not reachable by all initial rotten ones
# Multi source level order BFS
class Solution:

    # BFS with level order traversing in a 2D matrix
    def __bfs(self, i, j, grid: list[list[int]], rotten_minutes: list[list]) -> None:

        que = deque()
        que.append((i, j))

        level = 0

        while que:
            for _ in range(len(que)):
                x, y = que.popleft()
                direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        # Lets check for none first, if none we update instant (roting for the first time)
                        # Only check cells with good apples
                        if grid[nx][ny] == 1 and rotten_minutes[nx][ny] is None:
                            rotten_minutes[nx][ny] = level + 1
                            que.append((nx, ny))
                        # Already rotted. But can we rot it in shorter amount of time
                        # Multi source level order BFS, the node depth will be updated
                        elif grid[nx][ny] == 1 and rotten_minutes[nx][ny] > level + 1:
                            rotten_minutes[nx][ny] = level + 1
                            que.append((nx, ny))
            level += 1
        return
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Rotten Matrix, will be updated multiple times, we want to rot all our good oranges
        # As fast as possible -> Thats where multi-sorce BFS COMES
        # It also solves the sparse problem, can be multiple islands of ornage groups
        rotten_minutes = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    self.__bfs(i, j, grid, rotten_minutes)
        
        # A bit tricky part
        # We need to start at 0, that means assuming 0 days will take to rote oranges
        # Means no good orange in the begining
        max_min = 0
        for i in range(len(rotten_minutes)):
            for j in range(len(rotten_minutes[0])):
                if grid[i][j] == 1:
                    if rotten_minutes[i][j] is None:
                        return -1
                    else:
                        # The maximun value is the minimum number of days required to rot all the oranges
                        max_min = max(max_min, rotten_minutes[i][j])
        return max_min
