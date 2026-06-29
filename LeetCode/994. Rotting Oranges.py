# Corner case: There can be more than one rotten orange, so multi source BFS
# There can be isolated groups, like islands, making this a multi-graph. SO some oranges may never be rotten
# in multi-graph each good orange is not reachable by all initial rotten ones



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        time = {}
        que = deque()
        fresh = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    que.append((x,y))
                    time[(x,y)] = 0
                if grid[x][y] == 1:
                    fresh += 1
        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if (nx, ny) not in time and grid[nx][ny] == 1:
                        time[(nx,ny)] = time[(x,y)] + 1
                        que.append((nx, ny))
                        fresh -= 1
        # Return logic has corner case
        # If some frest remains means we have unreachable fresh or no rotten oranges
        if fresh != 0:
            return -1

        # Out time can be empty, that means there was no rotten oranges
        # We must check this after fresh, becasue there can be fresh oranges but not rotten
        # In that case we need to return -1, no amount of days will rot our oranges
        if time:
            return max(time.values())
        else:
            # We have no rotten or fresh orange, no days required at all
            return 0

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)