# Dijkstra Variant
# But instead of pushing distance, we push height of that grid cell
# Somewhere between dijkstra and prim's algo
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        source = (0,0)
        heap = [(grid[0][0], source)]
        visited = set()
        direction = [
            (1,0),
            (0,1),
            (-1, 0),
            (0,-1)
        ]
        max_cost = 0
        while heap:
            cost, (x, y) = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            max_cost = max(max_cost, grid[x][y])
            if x == len(grid) - 1 and y == len(grid) - 1:
                break
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if (nx, ny) not in visited:
                        heapq.heappush(heap, (grid[nx][ny], (nx,ny)))
        return max_cost


# Time Complexity: N^2.logE -> N^2logN
# Space Complexity: O(N^2) +