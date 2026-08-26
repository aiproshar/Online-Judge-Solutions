class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        que = deque()
        visited = set()
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # find a land
                if grid[i][j] == 1:
                    que.append((i, j))
                    visited.add((i, j))
                    break
            if que:
                break

        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            que.append((nx, ny))
                    else:
                        # sea blocks inside grid
                        perimeter += 1
                else:
                    # outside grid sea blocks
                    perimeter += 1
        return perimeter

"""
CCs
    - outbound is a perimeter
    - if neighbour is not soil we increase perimeter
    - if neighbour is visited aka grandparent, skip
    - no disconnected island, so one search is enough
TCs
    - all water
    - all island
    - single island in middle, corner

"""
# Time Complexity: O(V+E)
# Space Complexity: O(V) which is M*N


'''
Improved version, without BFS
All we need is to iterate over each node in the grid, check if the neighbours are water (including outbound)
'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for dx, dy in direction:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                            # out of bound perimeter
                            perimeter += 1
                        elif grid[nx][ny] == 0:
                            perimeter += 1
        return perimeter

# Time Complexity: O(M*N) == O(V)
# Space: O(1)